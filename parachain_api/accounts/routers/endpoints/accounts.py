from fastapi import APIRouter, Depends, Path

from core.dependencies.substrate_interface import get_substrate_interface_connection


router = APIRouter()


@router.get(
    '/balance/{account_hash}',
    description='Получить баланс аккаунта',
)
def get_balance(
    account_hash: str=Path(description='Хэш аккаунта'),
    substrate=Depends(get_substrate_interface_connection),
):
    try:
        result = substrate.query('System', 'Account', [f'{account_hash}'])

        return {'result': {'user_hash': account_hash, 'balance': result.value['data']['free']}}
    except Exception as e:
        return {'error': str(e)}


@router.get(
    '/',
    description='Получить список пользователей и их информацию'
)
def get_accounts(substrate=Depends(get_substrate_interface_connection)):
    try:
        result = substrate.query_map("System", "Account", max_results=100)
        accounts = []
        for account, account_info in result:
            accounts.append(f'{account.value}: {account_info.value}')

        return accounts
    except Exception as e:
        return {'error': str(e)}
