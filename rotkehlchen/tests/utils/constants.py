from rotkehlchen.assets.asset import Asset, EthereumToken
from rotkehlchen.chain.ethereum.types import string_to_ethereum_address
from rotkehlchen.constants.assets import A_EUR

A_RDN = EthereumToken('0x255Aa6DF07540Cb5d3d297f0D0D4D84cb52bc8e6')
A_GNO = EthereumToken('0x6810e776880C02933D47DB1b9fc05908e5386b96')
A_DAO = EthereumToken('0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413')
A_MKR = EthereumToken('0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2')
A_SNGLS = EthereumToken('0xaeC2E87E0A235266D9C5ADc9DEb4b2E29b54D009')
A_PAXG = EthereumToken('0x45804880De22913dAFE09f4980848ECE6EcbAf78')
A_ADAI = EthereumToken('0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d')
A_KCS = EthereumToken('0xf34960d9d60be18cC1D5Afc1A6F012A723a28811')
A_MCO = EthereumToken('0xB63B606Ac810a52cCa15e44bB630fd42D8d1d83d')
A_CRO = EthereumToken('0xA0b73E1Ff0B80914AB6fe0444E65848C4C34450b')
A_SUSHI = EthereumToken('0x6B3595068778DD592e39A122f4f5a5cF09C90fE2')
A_SDT2 = EthereumToken('0x73968b9a57c6E53d41345FD57a6E6ae27d6CDB2F')
A_QTUM = EthereumToken('0x9a642d6b3368ddc662CA244bAdf32cDA716005BC')
A_OCEAN = EthereumToken('0x967da4048cD07aB37855c090aAF366e4ce1b9F48')
A_GLM = EthereumToken('0x7DD9c5Cba05E151C895FDe1CF355C9A1D5DA6429')
A_BUSD = EthereumToken('0x4Fabb145d64652a948d72533023f6E7A623C7C53')
A_AMPL = EthereumToken('0xD46bA6D942050d489DBd938a2C909A5d5039A161')
A_SYN = EthereumToken('0x1695936d6a953df699C38CA21c2140d497C08BD9')
A_API3 = EthereumToken('0x0b38210ea11411557c13457D4dA7dC6ea731B88a')
A_MFT = EthereumToken('0xDF2C7238198Ad8B389666574f2d8bc411A4b7428')
A_DOLLAR_BASED = EthereumToken('0x68A118Ef45063051Eac49c7e647CE5Ace48a68a5')
A_BAND = EthereumToken('0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55')
A_YAM_V1 = EthereumToken('0x0e2298E3B3390e3b945a5456fBf59eCc3f55DA16')
A_AXS = EthereumToken('0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b')

A_LUNA = Asset('LUNA-2')
A_AIR2 = Asset('AIR-2')
A_SDC = Asset('SDC')
A_DOGE = Asset('DOGE')
A_NANO = Asset('NANO')
A_NEO = Asset('NEO')
A_SC = Asset('SC')
A_XMR = Asset('XMR')
A_DASH = Asset('DASH')
A_WAVES = Asset('WAVES')
A_EWT = Asset('EWT')
A_XTZ = Asset('XTZ')
A_BSV = Asset('BSV')
A_BCH = Asset('BCH')
A_CNY = Asset('CNY')
A_JPY = Asset('JPY')
A_ZEC = Asset('ZEC')
A_GBP = Asset('GBP')
A_CHF = Asset('CHF')
A_AUD = Asset('AUD')
A_CAD = Asset('CAD')
A_TRY = Asset('TRY')

ETH_ADDRESS1 = string_to_ethereum_address('0x5153493bB1E1642A63A098A65dD3913daBB6AE24')
ETH_ADDRESS2 = string_to_ethereum_address('0x4FED1fC4144c223aE3C1553be203cDFcbD38C581')
ETH_ADDRESS3 = string_to_ethereum_address('0x267FdC6F9F1C1a783b36126c1A59a9fbEBf42f84')

TX_HASH_STR1 = '0x9c81f44c29ff0226f835cd0a8a2f2a7eca6db52a711f8211b566fd15d3e0e8d4'
TX_HASH_STR2 = '0x1c81f44c29ff0236f835cd0a8a2f2a7eca6db52a711f8211b566fd15d3e0e899'
TX_HASH_STR3 = '0x3c81144c29f60236f735cd0a8a2f2a7e3a6db52a713f8211b562fd15d3e0e192'

MOCK_INPUT_DATA = b'123'
MOCK_INPUT_DATA_HEX = '0x313233'

DEFAULT_TESTS_MAIN_CURRENCY = A_EUR
