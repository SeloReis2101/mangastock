# from PIL import Image
# import numpy as np

def get_dominant_color(image_path, num_colors=1):
    # image = Image.open(image_path)
    # image = image.convert("RGB")

    # Resmi bir NumPy dizisine dönüştür
    # image_array = np.array(image)

    # Resmi düzleştir ve renkleri say
    # flat_image_array = image_array.reshape((-1, 3))
    # colors, counts = np.unique(flat_image_array, axis=0, return_counts=True)

    # Renkleri sayılarına göre sırala
    # sorted_colors = colors[np.argsort(-counts)]

    # En çok olan renkleri al
    # dominant_colors = sorted_colors[:6]

    # Renklerin ortalamasını al
    # average_color = np.mean(dominant_colors, axis=0).astype(int)

    # RGB renk formatına dönüştür
    # average_color_hex = "#{:02x}{:02x}{:02x}".format(*average_color)
    return "#FFFFFF"
    #return average_color_hex
