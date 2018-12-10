from django.shortcuts import render
from skin.toneExtract import *

# Create your views here.
def index(request):
    image =  imutils.url_to_image("https://i.pinimg.com/236x/61/28/32/612832c27fc272bc22fcc355b399715e--martin-schoeller-celebrity-portraits.jpg")

    # Resize image to a width of 250
    image = imutils.resize(image,width=250)

    #Show image
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.show()


    # Apply Skin Mask
    skin = extractSkin(image)

    plt.imshow(cv2.cvtColor(skin,cv2.COLOR_BGR2RGB))
    plt.show()



    # Find the dominant color. Default is 1 , pass the parameter 'number_of_colors=N' where N is the specified number of colors
    dominantColors = extractDominantColor(skin,hasThresholding=True)




    #Show in the dominant color information
    print("Color Information")
    colors = pretty_print_data(dominantColors)


    #Show in the dominant color as bar
    print("Color Bar")
    colour_bar = plotColorBar(dominantColors)
    plt.axis("off")
    plt.imshow(colour_bar)
    plt.show()

    return render(request,'index.html', {'colors':colors,'skin':skin})
