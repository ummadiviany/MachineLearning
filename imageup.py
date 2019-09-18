import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config( 
  cloud_name = "iiitrkvalley", 
  api_key = "353832435662295", 
  api_secret = "8NS9Xj9gHjfin8CCbT4Ga3C08yA" 
)
cloudinary.uploader.upload("C:/Users/lenovo/Desktop/c9.jpg", public_id = 'predected')

