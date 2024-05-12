from fastapi import APIRouter, Depends, Path
from substrateinterface import SubstrateInterface

from core.dependencies.substrate_interface import get_substrate_interface_connection


router = APIRouter()


@router.get(
    '/extrinsics/{block_hash}',
    description='Получить мета данные для определенного блока'
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
