import pytest
from ..base_model_test import BaseModelTest
from .sample_response import balance_response
from xendit.models import Balance, BalanceAccountType


class TestGetBalance(BaseModelTest):
    @pytest.fixture
    def default_balance_data(self):
        tested_class = Balance
        class_name = "Balance"
        method_name = "get"
        http_method_name = "get"
        params = (BalanceAccountType.CASH,)
        expected_correct_result = balance_response()
        return (
            tested_class,
            class_name,
            method_name,
            http_method_name,
            params,
            expected_correct_result,
        )

    @pytest.mark.parametrize(
        "mock_correct_response", [balance_response()], indirect=True
    )
    def test_return_balance_on_correct_params(
        self, mocker, mock_correct_response, default_balance_data
    ):
        self.run_success_return_test_on_xendit_instance(
            mocker, mock_correct_response, default_balance_data
        )

    def test_raise_xendit_error_on_response_error(
        self, mocker, mock_error_request_response, default_balance_data
    ):
        self.run_raises_error_test_on_xendit_instance(
            mocker, mock_error_request_response, default_balance_data
        )

    @pytest.mark.parametrize(
        "mock_correct_response", [balance_response()], indirect=True
    )
    def test_return_balance_on_correct_params_and_global_xendit(
        self, mocker, mock_correct_response, default_balance_data
    ):
        self.run_success_return_test_on_global_config(
            mocker, mock_correct_response, default_balance_data
        )

    def test_raise_xendit_error_on_response_error_and_global_xendit(
        self, mocker, mock_error_request_response, default_balance_data
    ):
        self.run_raises_error_test_on_global_config(
            mocker, mock_error_request_response, default_balance_data
        )
