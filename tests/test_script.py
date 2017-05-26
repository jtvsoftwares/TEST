
from jtv_test.script import MyClass

import mock
import pytest

@mock.patch('jtv_test.script.Service', autospec=True)
def test_f0(mock_service):

    jtv = MyClass()
    jtv.s = mock_service

    jtv.f0()

    mock_service.do_something.assert_called_with('Hello World!')

@mock.patch('jtv_test.script.Service', autospec=True)
def test_f1(mock_service):

    use_mock = True

    jtv = MyClass()

    if not use_mock:

        r = jtv.f1()
        assert [1, 2, 3, 4] == r

    else:

        mock_service.get_array.return_value = [0, 0, 0, 0]

        jtv.s = mock_service
        r = jtv.f1()

        assert [0, 0, 0, 0] == r


@pytest.mark.parametrize('test_json, test_result', [
    ({'rhs': 4, 'lhs': 6}, 24),
    pytest.mark.xfail(({'right': 5, 'left': 5}, 25))
])
@mock.patch('jtv_test.script.Service', autospec=True)
@mock.patch('jtv_test.script.json', autospec=True)
def test_f2(mock_json, mock_service, test_json, test_result):

    mock_json.loads.return_value = test_json
    mock_service.multiply.return_value = test_result

    jtv = MyClass()
    jtv.s = mock_service

    r = jtv.f2('JSON')

    assert test_result == r
    mock_json.loads.assert_called_with('JSON')
    mock_service.multiply.assert_called_with(test_json['rhs'], test_json['lhs'])
