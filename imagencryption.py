from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    try:
        image = Image.open(input_image_path)
        pixels = image.load()
        print(f"Encrypting image: {input_image_path}")

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

        image.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(encrypted_image_path, output_image_path, key):
    try:
        print(f"Decrypting image: {encrypted_image_path}")
        encrypt_image(encrypted_image_path, output_image_path, key)
        print(f"Image decrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

input_image = 'inputimg.jpg'  
encrypted_image = 'encrypted_image.png'
decrypted_image = 'decrypted_image.png'
key = 123  

# Debugging outputs
print("Starting encryption...")
encrypt_image(input_image, encrypted_image, key)
print("Starting decryption...")
decrypt_image(encrypted_image, decrypted_image, key)

