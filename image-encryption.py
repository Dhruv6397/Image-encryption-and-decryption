from PIL import Image
import numpy as np
import os

def generate_key(image_shape):
    return np.random.randint(0, 256, image_shape, dtype=np.uint8)

# Encrypt the image using XOR cipher
def encrypt_image(image_path, key, encrypted_image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    
    encrypted_image_np = np.bitwise_xor(image_np, key)
    
    encrypted_image = Image.fromarray(encrypted_image_np)
    encrypted_image.save(encrypted_image_path)

# Decrypt the image using XOR cipher
def decrypt_image(encrypted_image_path, key, decrypted_image_path):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_np = np.array(encrypted_image)
    
    decrypted_image_np = np.bitwise_xor(encrypted_image_np, key)
    
    
    decrypted_image = Image.fromarray(decrypted_image_np)
    decrypted_image.save(decrypted_image_path)

if __name__ == '__main__':
    image_path = 'input_image.png' 
    encrypted_image_path = 'encrypted_image.png'  
    decrypted_image_path = 'decrypted_image.png' 
    
    image = Image.open(image_path)
    key = generate_key(np.array(image).shape)
    
    encrypt_image(image_path, key, encrypted_image_path)
    print(f"Image encrypted and saved at {encrypted_image_path}")
    
    decrypt_image(encrypted_image_path, key, decrypted_image_path)
    print(f"Image decrypted and saved at {decrypted_image_path}")
