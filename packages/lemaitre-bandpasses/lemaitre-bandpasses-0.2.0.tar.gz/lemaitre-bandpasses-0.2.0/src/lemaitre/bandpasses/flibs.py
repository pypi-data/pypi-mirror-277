"""Standard filterlibs

We may want to add this to a sncosmo-like registry.
Not sure we really need that.

"""

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np

from bbf import FilterLib
from bbf.bspline import BSpline
from bbf import get_cache_dir



def ccdid_qid_to_rcid(ccdid, qid):
    """stolen from ztfimg.tools.

    .. note::
       Would love to use the original, but dask deps...
    """
    return 4*(ccdid - 1) + qid - 1


def get_filterlib(name='lemaitre', rebuild=False):
    """
    """
    cached_version_path = get_cache_dir().joinpath(f'{name}_flib.pkl')
    if cached_version_path.is_file() and not rebuild:
        fl = FilterLib.load(cached_version_path)
        return fl
    fl = rebuild_filterlib()
    return fl


def rebuild_filterlib():
    """
    """
    logging.info('rebuilding filterlib')
    fl = FilterLib(basis=np.arange(3000., 11010., 10.))


    # MegaCam6: the only tricky part is g, which requires
    # a higher resolution for the spatial spline basis
    logging.info('megacam6...')
    fl.insert(fl.fetch('megacam6::g', xy_size=40, xy_order=4),  'megacam6::g', sensor_id='*')
    fl.insert(fl.fetch('megacam6::r', xy_size=20, xy_order=2),  'megacam6::r', sensor_id='*')
    fl.insert(fl.fetch('megacam6::i2', xy_size=20, xy_order=2), 'megacam6::i2', sensor_id='*')
    fl.insert(fl.fetch('megacam6::z', xy_size=20, xy_order=2),  'megacam6::z', sensor_id='*')

    logging.info('megacam6 default (averaged) bandpasses')
    fl.insert(fl.fetch('megacam6::g', average=True),  'megacam6::g', average=True)
    fl.insert(fl.fetch('megacam6::r', average=True),  'megacam6::r', average=True)
    fl.insert(fl.fetch('megacam6::i2', average=True), 'megacam6::i2', average=True)
    fl.insert(fl.fetch('megacam6::z' , average=True),  'megacam6::z', average=True)

    logging.info('megacampsf default (averaged) bandpasses [used in JLA]')
    fl.insert(fl.fetch('megacampsf::g', average=True, radius=0.),  'megacampsf::g', average=True)
    fl.insert(fl.fetch('megacampsf::r', average=True, radius=0.),  'megacampsf::r', average=True)
    fl.insert(fl.fetch('megacampsf::i', average=True, radius=0.), 'megacampsf::i', average=True)
    fl.insert(fl.fetch('megacampsf::z' , average=True, radius=0.),  'megacampsf::z', average=True)

    logging.info('HSC')
    fl.insert(fl.fetch('hsc::g', xy_size=20, xy_order=2), 'hsc::g', sensor_id='*')
    fl.insert(fl.fetch('hsc::r', xy_size=20, xy_order=2), 'hsc::r', sensor_id='*')
    fl.insert(fl.fetch('hsc::r2', xy_size=20, xy_order=2), 'hsc::r2', sensor_id='*')
    fl.insert(fl.fetch('hsc::i', xy_size=20, xy_order=2), 'hsc::i', sensor_id='*')
    fl.insert(fl.fetch('hsc::i2', xy_size=20, xy_order=2), 'hsc::i2', sensor_id='*')
    fl.insert(fl.fetch('hsc::z', xy_size=20, xy_order=2), 'hsc::z', sensor_id='*')
    fl.insert(fl.fetch('hsc::Y', xy_size=20, xy_order=2), 'hsc::Y', sensor_id='*')

    logging.info('HSC default (averaged) bandpasses')
    fl.insert(fl.fetch('hsc::g', average=True), 'hsc::g', average=True)
    fl.insert(fl.fetch('hsc::r', average=True), 'hsc::r', average=True)
    fl.insert(fl.fetch('hsc::r2', average=True), 'hsc::r2', average=True)
    fl.insert(fl.fetch('hsc::i', average=True), 'hsc::i', average=True)
    fl.insert(fl.fetch('hsc::i2', average=True), 'hsc::i2', average=True)
    fl.insert(fl.fetch('hsc::z', average=True), 'hsc::z', average=True)
    fl.insert(fl.fetch('hsc::Y', average=True), 'hsc::Y', average=True)


    # for ZTF, we have basically two models: one for single coatings and another
    # for the double coatings. Both include the transforms for the entire filter set.
    #
    logging.info('ZTF')
    # Single coating
    sensor_id = ccdid_qid_to_rcid(1, 1) + 1
    bp_g = fl.fetch('ztf::g', xy_size=20, xy_order=2, sensor_id=sensor_id)
    bp_r = fl.fetch('ztf::r', xy_size=20, xy_order=2, sensor_id=sensor_id)
    bp_I = fl.fetch('ztf::I', xy_size=20, xy_order=2, sensor_id=sensor_id)

    for ccdid in [1, 2, 3, 4, 13, 14, 15, 16]:
        for qid in range(1, 5):
            sensor_id = ccdid_qid_to_rcid(ccdid, qid) + 1
            fl.insert(bp_g, 'ztf::g', sensor_id=sensor_id)
            fl.insert(bp_r, 'ztf::r', sensor_id=sensor_id)
            fl.insert(bp_I, 'ztf::I', sensor_id=sensor_id)

    # Double coating
    sensor_id = ccdid_qid_to_rcid(5, 1) + 1
    bp_g = fl.fetch('ztf::g', xy_size=20, xy_order=2, sensor_id=sensor_id)
    bp_r = fl.fetch('ztf::r', xy_size=20, xy_order=2, sensor_id=sensor_id)
    bp_I = fl.fetch('ztf::I', xy_size=20, xy_order=2, sensor_id=sensor_id)

    for ccdid in [5, 6, 7, 8, 9, 10, 11, 12]:
        for qid in range(1, 5):
            sensor_id = ccdid_qid_to_rcid(ccdid, qid) + 1
            fl.insert(bp_g, 'ztf::g', sensor_id=sensor_id)
            fl.insert(bp_r, 'ztf::r', sensor_id=sensor_id)
            fl.insert(bp_I, 'ztf::I', sensor_id=sensor_id)

    logging.info('ZTF default (averaged) bandpasses')
    fl.insert(fl.fetch('ztf::g', average=True), 'ztf::g', average=True)
    fl.insert(fl.fetch('ztf::r', average=True), 'ztf::r', average=True)
    fl.insert(fl.fetch('ztf::I', average=True), 'ztf::I', average=True)



    # dump it to cache
    cache_dir = get_cache_dir()
    # dst = cache_dir.joinpath('lemaitre_flib.hdf5')
    # fl.to_hdf5(dst, compression='lzf')
    dst = cache_dir.joinpath('lemaitre_flib.pkl')
    logging.info(f'to cache -> {dst}')
    fl.save(dst)

    logging.info('done')

    return fl
