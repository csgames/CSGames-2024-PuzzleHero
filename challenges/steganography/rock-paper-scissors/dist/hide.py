from PIL import Image

original_img = Image.open('org_rps.png')
original_pixels = original_img.load()

encoded_img = Image.new(original_img.mode, original_img.size)
encoded_pixels = encoded_img.load()

msg = 'flag{h1dd3n_m3ss4g3_1s_b3tt3r_th@n_r0ck_p@p3r_sc1ss0rs}'
msg_index = 0
msg_length = len(msg)

for row in range(original_img.size[0]):
    for col in range(original_img.size[1]):
        red, green, blue, _ = original_pixels[row, col]

        if row == 0 and col == 0:
            encoded_pixels[row, col] = (msg_length, green, blue)
        elif msg_index < msg_length:
            ascii_value = ord(msg[msg_index])
            encoded_pixels[row, col] = (ascii_value, green, blue)
            msg_index += 1
        else:
            encoded_pixels[row, col] = (red, green, blue)

original_img.close()

encoded_img.save("rps.png")
encoded_img.close()
