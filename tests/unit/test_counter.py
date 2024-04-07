import unittest
from boto3 import resource

from moto import mock_aws
from counter import read_counter


# Create your inputs
# Execute the code, capturing the output
# Compare the output with an expected result

get_visits = read_counter.get_visits
initialise_visits = read_counter.initialise_visits
update_counter = read_counter.update_counter

@mock_aws
class TestVisitsFunctions(unittest.TestCase):

    def setUp(self):
        dynamodb = resource('dynamodb')
        table_name = 'Visits'
        self.table = dynamodb.create_table(TableName=table_name,
                KeySchema=[{'AttributeName': 'id','KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'id','AttributeType': 'N'}],
                BillingMode= 'PAY_PER_REQUEST')
        
        initialise_visits(self.table)
        self.test_data = {'id':0,'visits':0}
        assert self.test_data == self.test_data
    
    
    def test_data_is_correct(self):
        response = self.table.get_item(Key={'id':0})
        db_data = response['Item']
        assert db_data == {'id':0,'visits':0}

    def test_increment_visit(self):
        visits = get_visits(self.table)
        assert visits == self.test_data["visits"]

    def tearDown(self):
        del self.test_data
        del self.table
    
        
if __name__ == '__main__':
    unittest.main()