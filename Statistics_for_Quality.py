
class Statistics_for_Quality(object):
       # percentage_Range_high = 90% -10%
    def percentage_Range_high(self,image):
        return np.percentile(image.ravel(), 90) - np.percentile(image.ravel(), 10)
    
    # percentage_Range_middle = 70% -30%
    def percentage_Range_middle(self,image):
        return np.percentile(image.ravel(), 70) - np.percentile(image.ravel(), 30)
    
    # high_pixel_ratio
    def high_pixel_ratio(self,image):
        return len(image[image > np.percentile(image.ravel(), 90)]) *1.0/ int(image.shape[0]*image.shape[1])
    
    # low_pixel_ratio
    def low_pixel_ratio(self,image):
        return len(image[image < np.percentile(image.ravel(), 10)]) *1.0/ int(image.shape[0]*image.shape[1])
    
    # Coefficient_of_variation= std / mean
    def Coefficient_of_variation(self,image):
        return image.std() / image.mean()

    # distributed_skewtest
    def distributed_skewtest(self,image):
        return stats.skewtest(image.ravel())[0]

    # distributed_kurtosis
    def distributed_kurtosis(self,image):
        return stats.kurtosistest(image.ravel())[0]

    # var
    def pixel_var(self,image):
        return np.var(image.ravel())

    def all_Statistics(self,value):
        return  self.percentage_Range_high(value),self.percentage_Range_middle(value),self.high_pixel_ratio(value),\
                self.low_pixel_ratio(value),self.Coefficient_of_variation(value),\
                self.distributed_skewtest(value),self.distributed_kurtosis(value),self.pixel_var(value)
