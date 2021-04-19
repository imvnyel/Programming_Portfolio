
'''Amazing! We built out a whole marketplace with buyers, sellers, art, and listings!

Here are some more things you could try:

-Add a WALLET instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
-Create a WISHLIST for your clients, things that are listed but they’re not sure if they should purchase just yet.
-Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.'''

class Art:
  def __init__(self, artist, title, year, medium, owner):
    self.artist = artist
    self.title = title
    self.year = year
    self.medium = medium
    self.owner = owner
    
    
  def __str__(self):
    output = '{artist}. "{title}". {year}, {medium}. {owner}, {location}.'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)
    return output
  
class Marketplace:
  listings = []
  def __init__(self):
    #self.listings = []
    return
    
  def add_listing(self, new_listing):
    self.new_listing = new_listing
    self.listings.append(self.new_listing)
    return
    
  def remove_listing(self, listing):
    self.listing = listing
    self.listings.remove(self.listing)
    return
  
  def show_listings(self):
    for i in self.listings:
      pass
      return i

  
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self, artwork, price):
    self.artwork = artwork
    self.price = price
    if self.artwork.owner.name == self.name:
      list_it = Listing(self.artwork, self.price, self.name)
      return veneer.add_listing(list_it)
    else:
      print("Yo bro, you cant sell that, it dont belong to you fam slice")
      
  def buy_artwork(self, artwork):
    self.artwork = artwork
    if self.artwork.owner.name != self.name:
      print('Seller'.center(15), '     ', 'Buyer'.center(30))
      print(self.artwork.owner.name.center(20), '--->'.center(5), self.name.center(20))
      for listing in veneer.listings:
        art_listing = listing
        if self.artwork == art_listing.art:
          self.artwork.owner = self
          veneer.remove_listing(art_listing)
    return print(self.artwork)
        
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    return
  
  def __str__(self):
    output = '{artwork_name}: {artwork_price}'.format(artwork_name=self.art.title, artwork_price=self.price) 
    return output
  

veneer = Marketplace()
edytta = Client('Edytta Halpirt', 'Private Collection', False)
moma = Client('MOMA', 'New York', True)
vatican = Client('Vatican', 'Vatican City', True)
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', '1910', 'oil on canvas', edytta) 
in_the_fog = Art('Monet, Claude', 'Vétheuil in the Fog', '1879', 'oil on canvas', vatican)




edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
print('Artwork for sale:\n'.center(40))
print(veneer.show_listings())
print('\n','Sold Artwork:'.center(40))
moma.buy_artwork(girl_with_mandolin)
print('\n','Artwork for sale:\n'.center(40))
print(veneer.show_listings())
