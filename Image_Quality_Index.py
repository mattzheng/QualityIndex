class Image_Quality_Index():
    
    def __init__(self, image_resize):
        self.image_resize = image_resize

    # grayscale_diff
    def grayscale_diff(self,image):
        diff_value = []
        for i in range(1,len(image.ravel())):
            diff_value.append(int(image.ravel()[i]) - int(image.ravel()[i-1])) 
        return math.log(np.var(diff_value))

    # grayscale_diff_Statistics
    def grayscale_diff_Statistics(self,image):
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return [self.grayscale_diff(image_gray)] + list(Statistics_Quality.all_Statistics(image_gray))
    
    # Laplacian_Ambiguity
    def Laplacian_Ambiguity(self,image):
        Laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
        return Laplacian_var
    
    # HSL(Hue),(Saturation),(Lightness)
    def HLS_for_Quality(self,image):
        Hue_values = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)[:,:,0]
        Saturation_value = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)[:,:,1]
        Saturation_Lightness = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)[:,:,2]
        return  Statistics_Quality.all_Statistics(Hue_values),\
                Statistics_Quality.all_Statistics(Saturation_value),\
                Statistics_Quality.all_Statistics(Saturation_Lightness)
    
    # Image_Basic_Attributes
    def Image_Basic_Attributes(self,userlist):
        image = cv2.imread(userlist)
        heigh_image,width_image,deep_image = float(image.shape[0]),float(image.shape[1]),float(image.shape[2]) 
        width_heigh_ritio = float(image.shape[1]) / float(image.shape[0])
        image_size_kb = float(os.path.getsize(userlist) ) /1024

    # Quality_Composite_Index
    def Quality_Composite_Index(self,userlist):
        # base
        image,heigh_image,width_image \
        ,deep_image,width_heigh_ritio,image_size_kb \
            = self.Image_Basic_Attributes(userlist)
        image = cv2.resize(image,(self.image_resize,self.image_resize),interpolation=cv2.INTER_CUBIC)
        # rbind
        temp_for_HLS = []
        temp_for_HLS.extend([heigh_image,width_image,deep_image,width_heigh_ritio,image_size_kb,self.Laplacian_Ambiguity(image)])
        temp_for_HLS.extend(self.grayscale_diff_Statistics(image))
        [temp_for_HLS.extend(temp_HLS) for temp_HLS in self.HLS_for_Quality(image)]
        return temp_for_HLS