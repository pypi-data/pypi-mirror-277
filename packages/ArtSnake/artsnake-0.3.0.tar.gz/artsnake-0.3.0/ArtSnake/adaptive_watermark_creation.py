import cv2
import numpy as np

# Main function to perform the entire watermark embedding process
def watermark_embedding(image, watermark, debug=False):
    if debug:
        print('Original image shape:', image.shape)
        print('Watermark shape:', watermark.shape)
    salient_map = salient_region_detection(image, debug=debug)
    if debug:
        print('Saliency map shape:', salient_map.shape)
    embedding_region = adaptive_selection_of_embedding_region(image, salient_map, watermark.shape, debug=debug)
    if debug:
        print('Embedding region shape:', embedding_region.shape)
    final_image = adaptive_visible_watermark_embedding(image, watermark, embedding_region, debug=debug)
    if debug:
        print('Final image shape:', final_image.shape)
    return final_image

# Function to detect salient regions
def salient_region_detection(image, debug=False):
    superpixels = k_means_clustering(image)
    if debug:
        print('Number of superpixels:', len(superpixels))
    corner_points = extract_corner_points(image)
    if debug:
        print('Number of corner points:', len(corner_points))
    polygon_S = construct_minimum_polygon(corner_points)
    if debug:
        print('Number of polygon S points:', len(polygon_S))
    saliency_scores = []
    for Ri in superpixels:
        sigma = estimate_sigma(image)
        Ni, wi = calculate_scaling_factor(Ri, superpixels, sigma)
        di = sum_of_squared_distances(Ri, superpixels)
        fi = wi * di
        Si = fi * Ni**(-1)
        if debug:
            print('Ni:', Ni, 'wi:', wi, 'di:', di, 'fi:', fi, 'Si:', Si)
        saliency_scores.append(Si)
    normalized_scores = normalize_saliency_scores(saliency_scores)
    saliency_map = create_saliency_map(image, superpixels, normalized_scores)
    return saliency_map

# Function to adaptively select the embedding region
def adaptive_selection_of_embedding_region(image, salient_map, watermark_size, debug=False):
    nonsalient_regions = get_nonsalient_regions(image, salient_map)
    subblocks = segment_into_subblocks(nonsalient_regions, watermark_size)
    if debug:
        print('Number of subblocks:', len(subblocks))
    texture_complexities = []
    gray_value_features = []
    for block in subblocks:
        H_G = gaussian_filter(block)
        G = laplacian_transform(H_G)
        G_B = otsu_binarization(G)
        M = morphological_closing(G_B)
        L_i = count_boundary_pixels(M, block)
        p_i = L_i / block.size
        texture_complexities.append(p_i)
    for block in subblocks:
        a_i = calculate_average_gray_level(block)
        y_i = 127 - a_i if a_i < 127 else a_i - 127
        gray_value_features.append(y_i)
    feature_values = [p_i / y_i for p_i, y_i in zip(texture_complexities, gray_value_features)]
    smoothest_block_index = feature_values.index(min(feature_values))
    embedding_region = subblocks[smoothest_block_index]
    return embedding_region

# Function to embed the watermark adaptively
def adaptive_visible_watermark_embedding(image, watermark, embedding_region, debug=False):
    yuv_image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    Y, U, V = cv2.split(yuv_image)
    J = calculate_jnd_matrix(Y)
    omega = estimate_omega(Y)
    I_w = Y.copy()
    for i in range(watermark.shape[0]):
        for j in range(watermark.shape[1]):
            W_ij = watermark[i, j]
            B_i = embedding_region[i*2:(i+1)*2, j*2:(j+1)*2]
            if W_ij == 0:
                continue
            elif W_ij == 1:
                P1, P2, P3, P4 = B_i.flatten()
                a_i = (P1 + P2) / 2
                a_j = (P3 + P4) / 2
                beta_i = np.arctan(a_j / a_i) + (np.pi / 4)
                alpha_i = calculate_texture_complexity(B_i)
                gamma_i = alpha_i / (beta_i - 1)
                gamma_i = normalize_gamma(gamma_i)
                for x in range(B_i.shape[0]):
                    for y in range(B_i.shape[1]):
                        I_ij = Y[i*2 + x, j*2 + y]
                        D_i = abs(W_ij - I_ij)
                        if D_i < J[x, y]:
                            if I_ij < 127:
                                I_w[i*2 + x, j*2 + y] = I_ij + omega * J[x, y]
                            else:
                                I_w[i*2 + x, j*2 + y] = I_ij - omega * J[x, y]
                        else:
                            I_w[i*2 + x, j*2 + y] = I_ij
    watermarked_image = cv2.merge([I_w, U, V])
    final_image = cv2.cvtColor(watermarked_image, cv2.COLOR_YUV2RGB)
    return final_image

# Helper functions
def get_nonsalient_regions(image, salient_map):
    nonsalient_mask = (salient_map == 0)
    nonsalient_regions = image * nonsalient_mask
    return nonsalient_regions

def segment_into_subblocks(nonsalient_regions, watermark_size):
    subblocks = []
    for i in range(0, nonsalient_regions.shape[0], watermark_size[0]):
        for j in range(0, nonsalient_regions.shape[1], watermark_size[1]):
            block = nonsalient_regions[i:i+watermark_size[0], j:j+watermark_size[1]]
            if block.shape == watermark_size:
                subblocks.append(block)
    return subblocks

def gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def laplacian_transform(image):
    return cv2.Laplacian(image, cv2.CV_64F)

def otsu_binarization(image):
    image_float = image.astype(np.float64)
    image_float = np.clip(image_float, 0, 255)
    image_uint8 = np.uint8(image_float)
    gray = cv2.cvtColor(image_uint8, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

def morphological_closing(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

def count_boundary_pixels(boundary_map, block):
    return np.sum(boundary_map[:block.shape[0], :block.shape[1]] > 0)

def calculate_average_gray_level(block):
    return np.mean(block)

def normalize_saliency_scores(scores):
    min_score = min(scores)
    max_score = max(scores)
    return [(score - min_score) / (max_score - min_score) * 255 for score in scores]

def create_saliency_map(image, superpixels, normalized_scores):
    saliency_map = np.zeros_like(image)
    for i, Ri in enumerate(superpixels):
        saliency_map[Ri] = normalized_scores[i]
    return saliency_map

def calculate_jnd_matrix(Y):
    J = np.zeros_like(Y)
    for i in range(Y.shape[0]):
        for j in range(i+1, Y.shape[1]):
            jnd = jensen_shannon_divergence(Y[i], Y[j])
            J[i, j] = J[j, i] = jnd
    return J

def jensen_shannon_divergence(p, q):
    m = 0.5 * (p + q)
    return 0.5 * (entropy(p, m) + entropy(q, m))

def entropy(p, q):
    return -np.sum(p * np.log2(q))

def calculate_texture_complexity(block):
    H_G = gaussian_filter(block)
    G = laplacian_transform(H_G)
    G_B = otsu_binarization(G)
    M = morphological_closing(G_B)
    L_i = count_boundary_pixels(M, block)
    p_i = L_i / block.size
    return p_i

def normalize_gamma(gamma_i):
    gamma_min, gamma_max = 0.3, 0.7
    return (gamma_i - gamma_i.min()) / (gamma_i.max() - gamma_i.min()) * (gamma_max - gamma_min) + gamma_min

def k_means_clustering(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    data = np.float32(gray.reshape(-1, 1))
    num_clusters = 20
    ret, labels, centers = cv2.kmeans(data, num_clusters, None, criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)
    labels = labels.reshape(gray.shape)
    masks = []
    for i in range(num_clusters):
        mask = np.where(labels == i, 255, 0).astype(np.uint8)
        masks.append(mask)
    return masks

def extract_corner_points(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    corner_points = []
    for contour in contours:
        for point in contour:
            if cv2.isContourConvex(contour):
                corner_points.append(point[0])
    return corner_points

def construct_minimum_polygon(corner_points):
    polygon = np.array(corner_points, dtype=np.int32)
    min_polygon = cv2.convexHull(polygon)
    return min_polygon

def calculate_scaling_factor(Ri, superpixels, sigma=1.0):
    Ni = 0
    for Rj in superpixels:
        wi = 1 if np.isin(Ri, Rj).any() else 0
        LMij = calculate_shortest_path(Ri, Rj)
        Ni += np.exp(-LMij / (sigma**2)) * wi
    return Ni, wi

def calculate_polygon_area(polygon):
    polygon_points = np.array(polygon, dtype=np.float32)
    return cv2.contourArea(polygon_points)

def sum_of_squared_distances(Ri, superpixels):
    di = 0
    for Rj in superpixels:
        di += np.sum((np.array(Ri) - np.array(Rj))**2)
    return di

def calculate_shortest_path(Ri, Rj):
    return np.linalg.norm(np.array(Ri) - np.array(Rj))

def distance_between_masks(mask1, mask2):
    difference = mask1 - mask2
    absolute_difference = np.abs(difference)
    sum_of_absolute_difference = np.sum(absolute_difference)
    average_distance = sum_of_absolute_difference / (mask1.size * mask1.itemsize)
    return average_distance

def estimate_sigma(image, fraction=0.1):
    height, width = image.shape[:2]
    diagonal_length = np.sqrt(height**2 + width**2)
    sigma = fraction * diagonal_length
    return sigma

def estimate_omega(Y):
    hist, _ = np.histogram(Y, bins=256, range=(0, 255))
    hist = hist / np.sum(hist)
    omega = np.sum(hist[1:] * np.arange(1, 256))
    return omega

if __name__ == '__main__':
    image = cv2.imread('ArtSnake/example.jpg')
    watermark = cv2.imread('ArtSnake/watermark.png')
    final_image = watermark_embedding(image, watermark, debug=True)
    cv2.imshow('Watermarked Image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()