from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url= 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup= soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "_3O0U0u"})
#print(len(containers)) #displays no. of products in the first page of flipkart

#print(soup.prettify(containers[0])) # prettify brings html code in a organized format (I kept this in notepad)

container= containers[0]
#print(container.div.img["alt"])# scripting product name

price= container.findAll("div", {"class": "_1uv9Cb"})
#print(price[0].text) # scripting product price and discounts

ratings= container.findAll("div", {"class": "niH0FQ _36Fcw_"})
#print(ratings[0].text) # scripting product ratings and reviews



#NOW WE WILL BE CREATING A FILE

filename="products.csv"
f= open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)


#NOW WE WILL USE A FOR LOOP TO SCRAP ALL THE PRODUCTS

for container in containers:
    product_name= container.div.img["alt"]

    price_container= container.findAll("div", {"class": "_1uv9Cb"}) #Here, "_1uv9Cb" taken from notepad textfile
    price=price_container[0].text.strip()

    rating_container= container.findAll("div", {"class": "niH0FQ _36Fcw_"}) #Here,  taken "niH0FQ _36Fcw_" from notepad textfile
    rating=rating_container[0].text

    #print("Product_name:" + product_name)
    #print("Price:" + price)
    #print("Ratings:" + rating)


    #CLEAN THE DATA
    #STRING PARSING
    trim_price=''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupee[1] # Replacing ₹ symbol by Rs.
    split_price = add_rs_price.split(" ")
    final_price=split_price[0]


    split_rating= rating.split("(") #Done inorder to remove No. of buyer's comments from reviews
    final_rating= split_rating[0]


    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")# output with 3 section clean data i.e product_name, final_price, final_rating
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n") #Writing output into product.csv file

f.close()
