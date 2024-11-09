import cv2
import matplotlib.pyplot as plt

# Membaca citra berwarna
image_color = cv2.imread('horse3.jpg')
image_color = cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk plotting

# Mengkonversi citra berwarna menjadi grayscale
image_gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY)

# Tampilkan citra asli (berwarna dan grayscale)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_color)
plt.title('Citra Berwarna')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_gray, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')
plt.show()
