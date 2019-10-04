# Place necessary comments and code here. 
#this is an instruction for users
tempt=-999999 # set a default temperatue to avoid the situation that there is no value for temperature
while(True):
    a=input("please select 1): Input the temperature; 2): Convert into centigrade; 3): Cloth suggestion; 4): Exit.\n") # This is an instruction for users
    if(a==1):
        tempt=input("please enter the temperature in Fahrenheit:")# get the temperrature from the keyboard
    elif(a==2):
        if(tempt>-999999):
            centi=(tempt-32.0)*5/9.0
            print "Centigrade is",round(centi,3)
        else:
            print("Please choose 1 first")
    elif(a==3):
        if(tempt>-99999 and tempt<55): #defining the temperature range for cold
          ClothingQualityCold=input("It's cold! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")  #getting user input for what quality of clothing they want
          if(ClothingQualityCold==1):
            print "this $1,095 expedition parka from Canada Goose will keep you warm, you dirty aristocrat         https://www.canadagoose.com/us/en/expedition-parka-801688665846.html?src=googleshopping&cmpid=6495103637&medium=cpc&source=google&agp=86411299348&cre=381782397258&kid=&mtype=&pla=&merchant_id=100661033&product_id=801688665846&country=US&gclid=CjwKCAjw29vsBRAuEiwA9s-0ByrMhYo39FZPbp4EnW0R_8kRY7EVywBxaI7VxtxZ9G1HsEtHSEm-WhoCmKwQAvD_BwE&gclsrc=aw.ds"

          elif(ClothingQualityCold==2):
            print "this $229 coat will keep you adequately warm, you practical, prudish New Englander  https://www.llbean.com/llb/shop/506673?originalProduct=78984&productId=1306114&attrValue_0=Charcoal%20Heather&pla1=0&mr%3AtrackingCode=A16A3E5E-9037-E611-80EE-00505694403D&mr%3AreferralID=NA&mr%3Adevice=c&mr%3AadType=plaonline&qs=3125251&gclid=CjwKCAjw29vsBRAuEiwA9s-0B2-q-Oxt0Z2-aQWbz6ZD3CKFwOD1vWIlqqL9DZyJDcZZ6hvKnQoEchoCGDEQAvD_BwE&gclsrc=aw.ds&SN=R90Test01&SS=A"
          
          elif(ClothingQualityCold==3):
            print"Comrade, this $70 coat will do the trick, as we do in the bosses like Alexander Berkman and Henry Clay Frick   https://shop.aramarkuniform.com/style?assort=catalog&style=401&sourcecode=156216&promo=YES&abc=d156216&utm_source=google&utm_medium=cpc&utm_campaign=GS+-+Aramark+DS+-+Shopping+-+Outerwear&utm_term=&gclid=CjwKCAjw29vsBRAuEiwA9s-0By0D8BX1ikEDtd_VMXY5ojf51l-sdGug6PNHhtMGQakKEE-r_BNjLBoCslsQAvD_BwE"
        elif(tempt>=55 and tempt<75):  #defining the temperature range for warm
          ClothingQualityWarm=input("It's warm! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")
          if(ClothingQualityWarm==1):
            print "These business casual items from Brooks Brothers will suit you, you dirty aristocrat https://magazine.brooksbrothers.com/business-casual-brooks-brothers/"
          
          elif(ClothingQualityWarm==2):
            print "These easy outfits from L.L. Bean will be fine, you practical, prudish New Englander https://www.llbean.com/shop/outfits/womens/index.html"
            
          elif(ClothingQualityWarm==3):
            print "Comrade, thess deals on ebay will do the trick, as we do in the bosses like Alexander Berkman and Henry Clay Frick https://www.ebay.com/b/Mens-Clothing/1059/bn_696958"
        elif(tempt>=75):  #defining the temperature range for hot
          ClothingQualityHot=input("It's hot! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")
          if(ClothingQualityHot==1):
            print "these Gucci swimwear options will suit your indolent lifestyle, aristocrat https://www.whowhatwear.com/luxury-swimwear-brands/slide16"

          elif(ClothingQualityHot==2):
            print "These boring swimsuits from L.L. Bean will allow you to have a moderate amount of fun, you practical, prudish New Englander https://www.llbean.com/llb/shop/516150?page=bathing-suits-and-swimwear&qs=3099119&Matchtype=e&msclkid=d12fadb8f7ef1b236086f02fa36402ec&gclid=CObGyO_lguUCFQKFgQodK4oH2A&gclsrc=ds"

          elif(ClothingQualityHot==3):
            print "Comrade, who needs clothes in this weather???"

    elif(a==4):
        print("thank you for your use!")
        break
    else:
        print("Please input the correct number")
