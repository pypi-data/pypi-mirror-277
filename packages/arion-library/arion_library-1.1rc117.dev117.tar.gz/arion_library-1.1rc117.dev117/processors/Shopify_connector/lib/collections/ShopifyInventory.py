from ..ShopifyConnector import ShopifyConnector
import requests
import json
from processors.Shopify_connector.lib.collections.graphql_queries import (
    get_inventory_levels_query,
    get_inventory_quantity_query,
    get_inventory_quantity_multiple_location,
    set_inventory_quantity_for_an_item
)
import logging

class GraphQLError(Exception):
    """Custom exception for GraphQL errors."""
    def __init__(self, errors):
        super().__init__("GraphQL query failed with errors")
        self.errors = errors

logger = logging.getLogger(__name__)

class ShopifyInventory(ShopifyConnector):
    """
    This class servers as abstracction for the shopify inventory collection
    NOTE : https://shopify.dev/docs/apps/fulfillment/inventory-management-apps/quantities-states#set-inventory-quantities-on-hand
    """

    def __init__(self, store_name, access_token):
        super().__init__(store_name, access_token)
    
    def fetch_inventory_levels(
        self,
        number_of_levels_to_show=3
        )->dict:
        """
        Retrieves all inventory levels from the specified collection.
        Uses Shopify's GRAPHQL Api
        """
        try:
                
            response = requests.post(
                self.store_url+"/graphql.json",
                headers=self.headers,
                data=json.dumps({
                    'query': get_inventory_levels_query(number_of_levels_to_show)
                })
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")
    
    def fetch_item_quantity_single_location(
        self,
        number_of_levels_to_show=3
        )->dict:
        """
        Retrieves all inventory quantity within a single location
        Uses Shopify's GRAPHQL Api
        """
        try:
                
            response = requests.post(
                self.store_url+"/graphql.json",
                headers=self.headers,
                data=json.dumps({
                    'query': get_inventory_quantity_query(number_of_levels_to_show)
                })
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")

    def fetch_item_quantity_multiple_location(
        self,
        inventoryItemId,
        number_of_levels_to_show=3
        )->dict:
        """
        Retrieves all inventory quantity within multiple locations
        Uses Shopify's GRAPHQL Api
        """
        try:
                
            response = requests.post(
                self.store_url+"/graphql.json",
                headers=self.headers,
                data=json.dumps({
                    'query': get_inventory_quantity_multiple_location(inventoryItemId,number_of_levels_to_show)
                })
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")
        
    def set_item_quantity(
        self,
        item_id:str,
        location_id:str,
        quantity:int
        )->dict:
        """
        Updates an inventory quantity of a specific item_id
        Uses Shopify's GRAPHQL Api
        """
        try:
            response = requests.post(
                self.store_url+"/graphql.json",
                headers=self.headers,
                data=json.dumps({
                    'query': set_inventory_quantity_for_an_item(item_id, location_id, quantity)
                })
            )
            if 'errors' in response.json():
                raise GraphQLError(response.json()['errors'])
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")
        
    