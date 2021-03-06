import astropy.io.fits as fits

def test_cat_add():
    import ddosa
    import dataanalysis.core as da

    da.debug_output()

    ddosa.ScWData(input_scwid="066500230010.001").promote()

    print "was before",ddosa.CatExtract()
    a = ddosa.CatExtract(
        input_extra_sources=ddosa.SourceList(use_sources=[dict(name="NEW_added",ra=83,dec=22)]),
    )
    print "got back",a

    assert hasattr(a,'input_extra_sources')

    a.cached=False

    a.get()

    print a.cat.get_path()
    f=fits.open(a.cat.get_path())[1]
    print f.data['NAME']

    assert "NEW_added" in f.data['NAME']


import astropy.io.fits as fits

def test_cat_add_postimage():
    import ddosa
    import dataanalysis.core as da

    da.debug_output()

    ddosa.ScWData(input_scwid="066500230010.001").promote()

    sl=ddosa.SourceList(use_sources=[dict(name="NEW_added",ra=83,dec=22)])

    a = ddosa.CatExtract(
        input_extra_sources=sl,
    )
    a.promote()

    b = ddosa.CatForSpectraFromImaging(
        input_extra_sources=sl,
        use_minsig=10,
    )
    b.promote()


    a.cached=False
    b.cached=False

    b.get()

    print b.cat.get_path()
    f=fits.open(b.cat.get_path())[1]
    print f.data['NAME']

    assert "NEW_added" in f.data['NAME']


