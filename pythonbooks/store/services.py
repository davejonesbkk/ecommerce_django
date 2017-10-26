from amazon.api import AmazonAPI
amazon = AmazonAPI('AKIAIDXUF5PRV54ZYWLA', '/SNOi4FMMLdPMhJ9JSfBywZs7p0HFC5RayCMgO1j',
	'davejonesbkk-20')



def get_books():

	product = amazon.lookup(ItemId='B00KC6I06S')
	title = product.title 
	price = product.price_and_currency
	image = product.medium_image_url

	return title

