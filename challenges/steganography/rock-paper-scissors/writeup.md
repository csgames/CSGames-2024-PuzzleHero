# Rock paper scissors

Le jeu était en fait une fausse piste. Le flag se trouve dans l'image.

```py
from PIL import Image

encoded_img = Image.open('rps.png')
encoded_pixels = encoded_img.load()

msg = ''
msg_index = 0 


for row in range(encoded_img.size[0]):
    for col in range(encoded_img.size[1]):
        r = encoded_pixels[row,col][0]

        if col==0 and row==0:
	        msg_len = r
            
        elif msg_len>msg_index:
            msg =msg+ chr(r)
            msg_index = msg_index+1

encoded_img.close()

print(msg)
```

## Flag

`flag{h1dd3n_m3ss4g3_1s_b3tt3r_th@n_r0ck_p@p3r_sc1ss0rs}`