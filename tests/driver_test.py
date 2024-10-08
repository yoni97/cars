# import pytest
# from bson import ObjectId
# from repository.driver_repository import create_driver, get_driver_by_name, get_all_drivers, get_driver_by_id, update_driver
#
# @pytest.fixture
# def driver_repo(init_test_data):
#     return DriverRepository(init_test_data['drivers'])
#
# @pytest.fixture
# def test_create_driver(driver_repo):
#     driver_data = {
#         'passport': 'TEST123',
#         'first_name': 'Test',
#         'last_name': 'Driver',
#         'car_id': str(ObjectId()),
#         'address': {
#             'city': 'TestCity',
#             'street': 'TestStreet',
#             'state': 'TS'
#         }
#     }
#     driver_id = driver_repo.create(driver_data)
#     assert driver_id is not None
#     created_driver = driver_repo.read(driver_id)
#     assert created_driver['passport'] == 'TEST123'
#
# def test_read_driver(driver_repo):
#     drivers = driver_repo.list_all()
#     assert len(drivers) > 0
#     first_driver = drivers[0]
#     read_driver = driver_repo.read(first_driver['_id'])
#     assert read_driver is not None
#     assert read_driver['_id'] == first_driver['_id']
#
# def test_update_driver(driver_repo):
#     drivers = driver_repo.list_all()
#     first_driver = drivers[0]
#     update_data = {'first_name': 'UpdatedName'}
#     success = driver_repo.update(first_driver['_id'], update_data)
#     assert success
#     updated_driver = driver_repo.read(first_driver['_id'])
#     assert updated_driver['first_name'] == 'UpdatedName'
#
# def test_delete_driver(driver_repo):
#     driver_data = {
#         'passport': 'DELETE123',
#         'first_name': 'Delete',
#         'last_name': 'Driver',
#         'car_id': str(ObjectId()),
#         'address': {
#             'city': 'DeleteCity',
#             'street': 'DeleteStreet',
#             'state': 'DS'
#         }
#     }
#     driver_id = driver_repo.create(driver_data)
#     success = driver_repo.delete(driver_id)
#     assert success
#     deleted_driver = driver_repo.read(driver_id)
#     assert deleted_driver is None
#
# def test_list_all_drivers(driver_repo):
#     drivers = driver_repo.list_all()
#     assert isinstance(drivers, list)
#     assert len(drivers) > 0
#     for driver in drivers:
#         assert '_id' in driver
#         assert 'passport' in driver
#         assert 'first_name' in driver
#         assert 'last_name' in driver
#         assert 'car_id' in driver
#         assert 'address' in driver