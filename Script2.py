# Place necessary comments and code here. 
#this is an instruction for users
tempt=-999999 # set a default temperatue to avoid the situation that there is no value for temperature from user. There are two advantages: 1. If there is no default value, it is hard to find whether users input a value into the temperature, whcih will cause errors in the program; 2. Users can change it during the whole process. If this variable was defined in the loop, for every loop it will change again because of the definition so that it is hard to change the value by users.
while(True):
    a=input("please select 1): Input the temperature; 2): Convert into centigrade; 3): Clothing recommendations; 4): Exit.\n") # This is an instruction for users
    if(a==1):
        tempt=input("please enter the temperature in Fahrenheit:")# getting the temperrature from the keyboard
    elif(a==2):
        if(tempt>-999999):# Determining whether users input the temperature
            centi=(tempt-32.0)*5/9.0 # computing the centigrade
            print "Centigrade is",round(centi,3) # retaining three digits after the decimal point
        else:
            print("Please choose 1 first")
    elif(a==3):
        if(tempt==-999999):# Determining whether users input the temperature
            print("Please choose 1 first")
            continue
        if(tempt<55): #defining the temperature range for cold
          ClothingQualityCold=input("It's cold! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")  #getting user input for what quality of clothing they want
          if(ClothingQualityCold==1):
            print "this $1,095 expedition parka from Canada Goose will keep you warm, you dirty aristocrat         https://www.canadagoose.com/us/en/expedition-parka-801688665846.html?src=googleshopping&cmpid=6495103637&medium=cpc&source=google&agp=86411299348&cre=381782397258&kid=&mtype=&pla=&merchant_id=100661033&product_id=801688665846&country=US&gclid=CjwKCAjw29vsBRAuEiwA9s-0ByrMhYo39FZPbp4EnW0R_8kRY7EVywBxaI7VxtxZ9G1HsEtHSEm-WhoCmKwQAvD_BwE&gclsrc=aw.ds"# providing suggestions about clothes

          elif(ClothingQualityCold==2):
            print "this $229 coat will keep you adequately warm, you practical, prudish New Englander  https://www.llbean.com/llb/shop/506673?originalProduct=78984&productId=1306114&attrValue_0=Charcoal%20Heather&pla1=0&mr%3AtrackingCode=A16A3E5E-9037-E611-80EE-00505694403D&mr%3AreferralID=NA&mr%3Adevice=c&mr%3AadType=plaonline&qs=3125251&gclid=CjwKCAjw29vsBRAuEiwA9s-0B2-q-Oxt0Z2-aQWbz6ZD3CKFwOD1vWIlqqL9DZyJDcZZ6hvKnQoEchoCGDEQAvD_BwE&gclsrc=aw.ds&SN=R90Test01&SS=A"
          
          elif(ClothingQualityCold==3):
            print"Comrade, this $70 coat will do the trick, as we do in the bosses like Alexander Berkman and Henry Clay Frick   https://shop.aramarkuniform.com/style?assort=catalog&style=401&sourcecode=156216&promo=YES&abc=d156216&utm_source=google&utm_medium=cpc&utm_campaign=GS+-+Aramark+DS+-+Shopping+-+Outerwear&utm_term=&gclid=CjwKCAjw29vsBRAuEiwA9s-0By0D8BX1ikEDtd_VMXY5ojf51l-sdGug6PNHhtMGQakKEE-r_BNjLBoCslsQAvD_BwE"
          else:
              print("Please input the correct number")# avoiding users' wrong input
        elif(tempt>=55 and tempt<75):  #defining the temperature range for warm
          ClothingQualityWarm=input("It's warm! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")
          if(ClothingQualityWarm==1):
            print "These business casual items from Brooks Brothers will suit you, you dirty aristocrat https://magazine.brooksbrothers.com/business-casual-brooks-brothers/"
          
          elif(ClothingQualityWarm==2):
            print "These easy outfits from L.L. Bean will be fine, you practical, prudish New Englander https://www.llbean.com/shop/outfits/womens/index.html"
            
          elif(ClothingQualityWarm==3):
            print "Comrade, these deals on ebay will do the trick, as we do in the bosses like Alexander Berkman and Henry Clay Frick https://www.ebay.com/b/Mens-Clothing/1059/bn_696958"
          else:
              print("Please input the correct number")
        elif(tempt>=75):  #defining the temperature range for hot
          ClothingQualityHot=input("It's hot! Would you like 1) high, 2) medium, or 3) low quality clothing for this weather?")
          if(ClothingQualityHot==1):
            print "these Gucci swimwear options will suit your indolent lifestyle, aristocrat https://www.whowhatwear.com/luxury-swimwear-brands/slide16"

          elif(ClothingQualityHot==2):
            print "These boring swimsuits from L.L. Bean will allow you to have a moderate amount of fun, you practical, prudish New Englander https://www.llbean.com/llb/shop/516150?page=bathing-suits-and-swimwear&qs=3099119&Matchtype=e&msclkid=d12fadb8f7ef1b236086f02fa36402ec&gclid=CObGyO_lguUCFQKFgQodK4oH2A&gclsrc=ds"

          elif(ClothingQualityHot==3):
            print "Comrade, who needs clothes in this weather???"
          else:
              print("Please input the correct number")

            
    elif(a==4):
        print("thank you for your use!")# when users choose to exit, we give them a nice goodbye
        break
    else:
        print("Please input the correct number")# avoiding users' wrong input
