import logging 

from ..ShopifyConnector import ShopifyConnector
import requests

logger= logging.getLogger(__name__)

class ShopifyProducts(ShopifyConnector):

    def __init__(self, store_name, access_token):
        super().__init__(store_name, access_token)
        
        # self.products = self.get_products()

    def get_products(self):
        """
        Retrieves all products from the specified collection.
        Uses Shopify's REST Api
        """
        url = f"{self.store_url}/products.json"
        products = []
        try :
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                products = response.json()['products']
                if len(products) > 0 :
                    return products
                else:
                    return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")
    
    def get_product(
            self,
            product_id:str
            ):
        """
        Retrieves a specific product by its ID.
        Uses Shopify's REST Api
        """

        url = f"{self.store_url}/products/{product_id}.json"
        product = {}
        try :
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                product = response.json()['product']
                if len(product) > 0 :
                    return product
                else:
                    return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")

    def extract_id_from_sku(
            self,
            target_sku:str
            ):
        """
        Extracts the product ID from a given SKU.
        Uses Shopify's REST Api
        Args:
            target_sku (str): The SKU of the product.
        Returns:
            int | None: The product ID if found, None otherwise.
        Raises:
            requests.exceptions.RequestException: If there is an error making the API request.
        """
        
        target_sku = str(target_sku)
        try :
            products = self.products
            for product in products:
                for variant in product["variants"]:
                    if variant["sku"] == target_sku:
                        product_id = product["id"]
                        break
            if product_id:
                return product_id
            else:
                return  None

        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")

    def update_product(
            self,
            product_id:str,
            data:dict
            ):
        """
        Updates a product in the specified collection.
        Uses Shopify's REST Api
        """

        url = f"{self.store_url}/admin/api/2023-04/products/{product_id}.json"
        try :
            response = requests.put(url, json=data, headers=self.headers)
            if response.status_code == 200:
                logger.info("Product updated successfully")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")