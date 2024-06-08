from . import pet


class IsScannerVersionCorrect(pet.IsScannerVersionCorrect):

    passing = 'BBRCDEV_E02957',
    failing = 'BBRCDEV_E02948',
    scanner_info = {'Manufacturer': ['SIEMENS'],
                    'ManufacturersModelName': ['Biograph64', 'Biograph64_mCT'],
                    'SoftwareVersion(s)': ['VG62B']}
    __doc__ = pet.IsScannerVersionCorrect.__doc__


class HasUsableT1(pet.HasUsableT1):
    passing = 'BBRCDEV_E02957',
    failing = 'BBRCDEV_E02948',
    included_projects = ['testenv', 'ALFA_PLUS_V2', 'ALFA_PLUS2_V2',
                         'ALFA_PLUS_VX', 'ALFA_PLUS_V3', 'ALFA_PLUS2_V3']
    __doc__ = pet.HasUsableT1.__doc__


class IsInjectionTimeConsistent(pet.IsInjectionTimeConsistent):
    passing = 'BBRCDEV_E02957',
    failing = 'BBRCDEV_E02948',
    injection_times = {'t807': 80}

    __doc__ = pet.IsInjectionTimeConsistent.__doc__
    __doc__ = __doc__.replace(
        'Flutemetamol PET: 90 min ± 20%; Fluorodeoxyglucose PET: 45 min ± 20%',
        'TAU PET: 80 min ± 20%')
