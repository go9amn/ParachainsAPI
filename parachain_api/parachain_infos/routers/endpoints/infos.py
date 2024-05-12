from fastapi import APIRouter, Depends, Path
from substrateinterface import Keypair

from core.dependencies.substrate_interface import get_substrate_interface_connection
from parachain_infos.schemas.fee_info import FeeInfo

router = APIRouter()


@router.get(
    '/extrinsics/{block_hash}',
    description='Получить мета данные для блока по его хэшу'
)
def retrieve_extrinsics(
    substrate=Depends(get_substrate_interface_connection),
    block_hash=Path(description='Хэш сумма необходимого блока')
):
    extrinsics_data = []

    result = substrate.get_block(block_hash=block_hash)

    for extrinsic in result['extrinsics']:
        extrinsic_info = {}

        if 'address' in extrinsic.value:
            signed_by_address = extrinsic.value['address']
        else:
            signed_by_address = None

        extrinsic_info['pallet'] = extrinsic.value["call"]["call_module"]
        extrinsic_info['call'] = extrinsic.value["call"]["call_function"]
        extrinsic_info['signed_by'] = signed_by_address

        params_data = []
        for param in extrinsic.value["call"]['call_args']:
            param_info = {}
            param_info['name'] = param['name']
            param_info['value'] = param['value']

            if param['type'] == 'Balance':
                param_info['value'] = '{} {}'.format(param['value'] / 10 ** substrate.token_decimals,
                                                     substrate.token_symbol)

            params_data.append(param_info)

        extrinsic_info['params'] = params_data

        extrinsics_data.append(extrinsic_info)

    return extrinsics_data


@router.post(
    '/fee/{destination}',
    description='Узнать стоимость налога на транзакцию',
)
def retrieve_fee(
    request_body: FeeInfo,
    destination: str = Path(description='Хэш пользователя получателя'),
    substrate=Depends(get_substrate_interface_connection),
):
    keypair = Keypair.create_from_uri(f'//{request_body.name_for_keypair_by_uri}')

    call = substrate.compose_call(
        call_module='Balances',
        call_function='transfer',
        call_params={
            'dest': f'{destination}',
            'value': f'{request_body.value}',
        }
    )

    # Get payment info
    payment_info = substrate.get_payment_info(call=call, keypair=keypair)

    return {'result': {'destination': destination, 'payment_info': payment_info}}
