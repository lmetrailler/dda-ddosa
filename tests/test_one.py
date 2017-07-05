import glob
import os

import astropy.io.fits as fits

import ddosa
import dataanalysis.core as da


def test_scw():
    #da.debug_output()

    
    fa=ddosa.ScWData(input_scwid="066500230010.001")

    fa.get()

    print fa.scwpath


def test_gti():
#    da.debug_output()

    fa=ddosa.ibis_gti(assume=[
                            ddosa.ScWData(input_scwid="066500230010.001"),
                        ])
    fa.read_caches=[]
    

    fa.get()


def test_gti_cached():
    da.debug_output()

    fa = ddosa.ibis_gti(assume=[
        ddosa.ScWData(input_scwid="066500230010.001"),
    ])

    fa.get()


    # now get cached

    fb = ddosa.ibis_gti(assume=[
        ddosa.ScWData(input_scwid="066500230010.001"),
    ])

    fb.produce_disabled=True

    fb.get()


def test_image():
    #
    # da.debug_output()

    
    fa=ddosa.ii_skyimage(assume=[
                            ddosa.ScWData(input_scwid="066500230010.001"),
                        ])
    fa.read_caches=[]

    fa.get()


    print fa.skyima


def test_image_cached():
    fa = ddosa.ii_skyimage(assume=[
        ddosa.ScWData(input_scwid="066500230010.001"),
    ])

    fa.get()

    # now get cached


    fb = ddosa.ii_skyimage(assume=[
        ddosa.ScWData(input_scwid="066500230010.001"),
    ])

    fb.produce_disabled = True

    import time
    t0 = time.time()

    fb.get()

    assert time.time()-t0<3


def test_spectra():
    #da.debug_output()

    fa = ddosa.ii_spectra_extract(assume=[
        ddosa.ScWData(input_scwid="066500230010.001"),
        ddosa.SpectraBins(use_rmfpath="/data/resources/rmf_62bands.fits"),
    ])
    fa.read_caches = []

    fa.get()

    assert os.path.exists(fa.spectrum.get_path())

