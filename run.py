
folder = '/content/drive/MyDrive/pytti_test/images_out/default' #@param {type:"string"}

#@markdown ###the higher the next value, the longer the final video
#@markdown ###1 ≈ 2x, 2 ≈ 4x, 3 ≈ 8x etc.

times = 3 #@param {type:"slider", min:1, max:10, step:1}

#@markdown ###look for the result in your folder - output video and a new slow-motion image sequence


!python3 -m frame_interpolation.eval.interpolator_cli \
         --pattern $folder \
         --model_path /content/pretrained_models/film_net/Style/saved_model \
         --times_to_interpolate $times \
         --output_video
