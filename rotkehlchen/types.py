from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    NamedTuple,
    NewType,
    Optional,
    Tuple,
    Type,
    Union,
)

from eth_typing import ChecksumAddress
from hexbytes import HexBytes as Web3HexBytes

from rotkehlchen.errors import DeserializationError  # lgtm [py/unsafe-cyclic-import]  # noqa: E501
from rotkehlchen.fval import FVal
from rotkehlchen.utils.hexbytes import HexBytes
from rotkehlchen.utils.mixins.dbenum import DBEnumMixIn  # lgtm[py/unsafe-cyclic-import]
from rotkehlchen.utils.mixins.serializableenum import SerializableEnumMixin

from rotkehlchen.chain.substrate.types import KusamaAddress, PolkadotAddress  # isort:skip # lgtm [py/unsafe-cyclic-import]  # noqa: E501

ModuleName = Literal[
    'makerdao_dsr',
    'makerdao_vaults',
    'aave',
    'compound',
    'yearn_vaults',
    'yearn_vaults_v2',
    'uniswap',
    'adex',
    'loopring',
    'balancer',
    'eth2',
    'sushiswap',
    'liquity',
    'pickle_finance',
    'nfts',
]

# TODO: Turn this into some kind of light data structure and not just a mapping
# This is a mapping of module ids to human readable names
AVAILABLE_MODULES_MAP = {
    'makerdao_dsr': 'MakerDAO DSR',
    'makerdao_vaults': 'MakerDAO Vaults',
    'aave': 'Aave',
    'compound': 'Compound',
    'yearn_vaults': 'Yearn Vaults',
    'yearn_vaults_v2': 'Yearn V2 Vaults',
    'uniswap': 'Uniswap',
    'adex': 'AdEx',
    'loopring': 'Loopring',
    'balancer': 'Balancer',
    'eth2': 'Eth2',
    'sushiswap': 'Sushiswap',
    'liquity': 'Liquity',
    'pickle_finance': 'Pickle Finance',
    'nfts': 'NFTs',
}
DEFAULT_OFF_MODULES = {'makerdao_dsr', 'yearn_vaults', 'adex'}


IMPORTABLE_LOCATIONS = Literal[
    'cointracking.info',
    'cryptocom',
    'blockfi-transactions',
    'blockfi-trades',
    'nexo',
    'gitcoin',
    'shapeshift-trades',
    'uphold',
    'bisq',
]

UNISWAP_PROTOCOL = 'UNI-V2'
YEARN_VAULTS_V2_PROTOCOL = 'yearn_vaults_v2'
CURVE_POOL_PROTOCOL = 'curve_pool'


KnownProtocolsAssets = (
    UNISWAP_PROTOCOL,
    YEARN_VAULTS_V2_PROTOCOL,
    CURVE_POOL_PROTOCOL,
)


T_Timestamp = int
Timestamp = NewType('Timestamp', T_Timestamp)

T_TimestampMS = int
TimestampMS = NewType('TimestampMS', T_TimestampMS)

T_ApiKey = str
ApiKey = NewType('ApiKey', T_ApiKey)

T_ApiSecret = bytes
ApiSecret = NewType('ApiSecret', T_ApiSecret)

T_B64EncodedBytes = bytes
B64EncodedBytes = NewType('B64EncodedBytes', T_B64EncodedBytes)

T_B64EncodedString = str
B64EncodedString = NewType('B64EncodedString', T_B64EncodedString)

T_HexColorCode = str
HexColorCode = NewType('HexColorCode', T_HexColorCode)


class ExternalService(SerializableEnumMixin):
    ETHERSCAN = 0
    CRYPTOCOMPARE = 1
    BEACONCHAIN = 2
    LOOPRING = 3
    OPENSEA = 4
    COVALENT = 5


class ExternalServiceApiCredentials(NamedTuple):
    """Represents Credentials for various External APIs. Etherscan, Cryptocompare e.t.c.

    The Api in question must at least have an API key.
    """
    service: ExternalService
    api_key: ApiKey

    def serialize_for_db(self) -> Tuple[str, str]:
        return (self.service.name.lower(), self.api_key)


T_TradePair = str
TradePair = NewType('TradePair', T_TradePair)

T_EthAddres = str
EthAddress = NewType('EthAddress', T_EthAddres)

ChecksumEthAddress = ChecksumAddress

T_EVMTxHash = HexBytes
EVMTxHash = NewType('EVMTxHash', T_EVMTxHash)


def deserialize_evm_tx_hash(val: Union[Web3HexBytes, bytearray, bytes, str]) -> EVMTxHash:
    """Super lightweight wrapper to forward arguments to HexBytes and return an EVMTxHash

    HexBytes constructor handles the deserialization from whatever is given as input.

    May raise DeserializationError if there is an error at deserialization

    NB: Does not actually check that it's 32 bytes. This should happen at reading
    data from outside such as in the marshmallow field validation
    """
    return EVMTxHash(HexBytes(val))


def make_evm_tx_hash(val: bytes) -> EVMTxHash:
    """Super lightweight wrapper initialize an EVMTxHash from bytes

    No deserialization happens here

    NB: Does not actually check that it's 32 bytes. This should happen at reading
    data from outside such as in the marshmallow field validation
    """
    return EVMTxHash(HexBytes(val))


T_BTCAddress = str
BTCAddress = NewType('BTCAddress', T_BTCAddress)

T_Eth2PubKey = str
Eth2PubKey = NewType('Eth2PubKey', T_Eth2PubKey)

BlockchainAddress = Union[
    EthAddress,
    BTCAddress,
    ChecksumEthAddress,
    KusamaAddress,
    PolkadotAddress,
    str,
]
ListOfBlockchainAddresses = Union[
    List[BTCAddress],
    List[ChecksumEthAddress],
    List[KusamaAddress],
    List[PolkadotAddress],
]


T_Fee = FVal
Fee = NewType('Fee', T_Fee)

T_Price = FVal
Price = NewType('Price', T_Price)

T_AssetAmount = FVal
AssetAmount = NewType('AssetAmount', T_AssetAmount)

T_TradeID = str
TradeID = NewType('TradeID', T_TradeID)


T_EventType = str
EventType = NewType('EventType', T_EventType)


class EthereumTransaction(NamedTuple):
    """Represent an Ethereum transaction"""
    tx_hash: EVMTxHash
    timestamp: Timestamp
    block_number: int
    from_address: ChecksumEthAddress
    to_address: Optional[ChecksumEthAddress]
    value: int
    gas: int
    gas_price: int
    gas_used: int
    input_data: bytes
    nonce: int

    def serialize(self) -> Dict[str, Any]:
        result = self._asdict()  # pylint: disable=no-member
        result['identifier'] = self.identifier
        result['tx_hash'] = result['tx_hash'].hex()
        result['input_data'] = '0x' + result['input_data'].hex()

        # Most integers are turned to string to be sent via the API
        result['value'] = str(result['value'])
        result['gas'] = str(result['gas'])
        result['gas_price'] = str(result['gas_price'])
        result['gas_used'] = str(result['gas_used'])
        return result

    def __hash__(self) -> int:
        return hash(self.identifier)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EthereumTransaction):
            return False

        return hash(self) == hash(other)

    @property
    def identifier(self) -> str:
        return self.tx_hash.hex() + self.from_address + str(self.nonce)


class EthereumInternalTransaction(NamedTuple):
    """Represent an internal Ethereum transaction"""
    parent_tx_hash: EVMTxHash
    trace_id: int
    timestamp: Timestamp
    block_number: int
    from_address: ChecksumEthAddress
    to_address: Optional[ChecksumEthAddress]
    value: int

    def serialize(self) -> Dict[str, Any]:
        result = self._asdict()  # pylint: disable=no-member
        result['tx_hash'] = result['tx_hash'].hex()
        result['value'] = str(result['value'])
        return result

    def __hash__(self) -> int:
        return hash(self.identifier)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EthereumInternalTransaction):
            return False

        return hash(self) == hash(other)

    @property
    def identifier(self) -> str:
        return self.parent_tx_hash.hex() + str(self.trace_id)


class CovalentTransaction(NamedTuple):
    """Represent a transaction in covalent"""
    tx_hash: str
    timestamp: Timestamp
    block_number: int
    from_address: ChecksumEthAddress
    to_address: Optional[ChecksumEthAddress]
    value: int
    gas: int
    gas_price: int
    gas_used: int
    # Input data and nonce is decoded, default is 0x and 0, encoded in future
    input_data: str
    nonce: int

    def serialize(self) -> Dict[str, Any]:
        result = {
            'tx_hash': self.tx_hash,
            'timestamp': self.timestamp,
            'block_number': self.block_number,
            'from_address': self.from_address,
            'to_address': self.to_address,
            'value': self.value,
            'gas': self.gas,
            'gas_price': self.gas_price,
            'gas_used': self.gas_used,
            'input_data': self.input_data,
            'nonce': self.nonce,
        }

        return result

    def __hash__(self) -> int:
        return hash(self.identifier)

    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, CovalentTransaction):
            return False

        return hash(self) == hash(other)

    @property
    def identifier(self) -> str:
        return self.tx_hash + self.from_address.replace('0x', '') + str(self.nonce)


class SupportedBlockchain(Enum):
    """These are the blockchains for which account tracking is supported """
    ETHEREUM = 'ETH'
    ETHEREUM_BEACONCHAIN = 'ETH2'
    BITCOIN = 'BTC'
    KUSAMA = 'KSM'
    AVALANCHE = 'AVAX'
    POLKADOT = 'DOT'

    def get_address_type(self) -> Callable:
        if self in (SupportedBlockchain.ETHEREUM, SupportedBlockchain.AVALANCHE):
            return ChecksumEthAddress
        if self == SupportedBlockchain.ETHEREUM_BEACONCHAIN:
            return Eth2PubKey
        if self == SupportedBlockchain.BITCOIN:
            return BTCAddress
        if self == SupportedBlockchain.KUSAMA:
            return KusamaAddress
        if self == SupportedBlockchain.POLKADOT:
            return PolkadotAddress
        raise AssertionError(f'Invalid SupportedBlockchain value: {self}')

    def ens_coin_type(self) -> int:
        """Return the CoinType number according to EIP-2304, multichain address
        resolution for ENS domains.

        https://eips.ethereum.org/EIPS/eip-2304
        """
        if self == SupportedBlockchain.ETHEREUM:
            return 60
        if self == SupportedBlockchain.BITCOIN:
            return 0
        if self == SupportedBlockchain.KUSAMA:
            return 434
        if self == SupportedBlockchain.POLKADOT:
            return 354
        if self == SupportedBlockchain.AVALANCHE:
            return 9000
        raise AssertionError(f'Invalid SupportedBlockchain value: {self}')


class TradeType(DBEnumMixIn):
    BUY = 1
    SELL = 2
    SETTLEMENT_BUY = 3
    SETTLEMENT_SELL = 4

    @classmethod
    def deserialize(cls: Type['TradeType'], symbol: str) -> 'TradeType':
        """Overriding deserialize here since it can have different wordings for the same type
        so the automatic deserialization does not work
        """
        if not isinstance(symbol, str):
            raise DeserializationError(
                f'Failed to deserialize trade type symbol from {type(symbol)} entry',
            )

        if symbol in ('buy', 'LIMIT_BUY', 'BUY', 'Buy'):
            return TradeType.BUY
        if symbol in ('sell', 'LIMIT_SELL', 'SELL', 'Sell'):
            return TradeType.SELL
        if symbol in ('settlement_buy', 'settlement buy'):
            return TradeType.SETTLEMENT_BUY
        if symbol in ('settlement_sell', 'settlement sell'):
            return TradeType.SETTLEMENT_SELL

        # else
        raise DeserializationError(
            f'Failed to deserialize trade type symbol. Unknown symbol {symbol} for trade type',
        )


class Location(DBEnumMixIn):
    """Supported Locations"""
    EXTERNAL = 1
    KRAKEN = 2
    POLONIEX = 3
    BITTREX = 4
    BINANCE = 5
    BITMEX = 6
    COINBASE = 7
    TOTAL = 8
    BANKS = 9
    BLOCKCHAIN = 10
    COINBASEPRO = 11
    GEMINI = 12
    EQUITIES = 13
    REALESTATE = 14
    COMMODITIES = 15
    CRYPTOCOM = 16
    UNISWAP = 17
    BITSTAMP = 18
    BINANCEUS = 19
    BITFINEX = 20
    BITCOINDE = 21
    ICONOMI = 22
    KUCOIN = 23
    BALANCER = 24
    LOOPRING = 25
    FTX = 26
    NEXO = 27
    BLOCKFI = 28
    INDEPENDENTRESERVE = 29
    GITCOIN = 30
    SUSHISWAP = 31
    SHAPESHIFT = 32
    UPHOLD = 33
    BITPANDA = 34
    BISQ = 35
    FTXUS = 36


class AssetMovementCategory(DBEnumMixIn):
    """Supported Asset Movement Types so far only deposit and withdrawals"""
    DEPOSIT = 1
    WITHDRAWAL = 2


class BlockchainAccountData(NamedTuple):
    address: BlockchainAddress
    label: Optional[str] = None
    tags: Optional[List[str]] = None


class ExchangeApiCredentials(NamedTuple):
    """Represents Credentials for Exchanges

    The Api in question must at least have an API key and an API secret.
    """
    name: str  # A unique name to identify this particular Location credentials
    location: Location
    api_key: ApiKey
    api_secret: ApiSecret
    passphrase: Optional[str] = None


EXTERNAL_EXCHANGES: List = [
    Location.CRYPTOCOM,
    Location.BLOCKFI,
    Location.NEXO,
    Location.SHAPESHIFT,
    Location.UPHOLD,
    Location.BISQ,
]
EXTERNAL_LOCATION = [Location.EXTERNAL] + EXTERNAL_EXCHANGES
