"""
curves containing test data for the optimizer

USAGE

::
    from testdata.curves1 import curves_dct_f
    curves_dct = curves_dct_f()
    curves = curves_dct["curves"]
    
"""
from ..curves import ConstantProductCurve as CPC

def curves_dct_f():
    """
    collection of test curves for the optimizer
    
    :return: ``dict`` of curves
    """
    # ### Curves


    curves_dct = {}

    # #### Unlevered curves only

    # ##### Unlevered pair

    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 USDC
        CPC.from_univ2(pair="WETH/USDC", p=3000, k=3000*vol**2, fee=0, cid="1.1.1"),  
        
        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ2(pair="WETH/USDC", p=3500, k=3000*vol**2, fee=0, cid="1.1.2"),      
    ]
    curves_dct["unlevered_pair"] = curves


    # ##### Unlevered triangle

    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ2(pair="WETH/DAI", p=3000, k=3000*vol**2, fee=0, cid="1.2.1"),  

        # curve buys/sells DAI @ 1 USDC
        CPC.from_univ2(pair="DAI/USDC", p=1, k=3000**2 * vol**2, fee=0, cid="1.2.2"),  
        
        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ2(pair="WETH/USDC", p=3500, k=3500*vol**2, fee=0, cid="1.2.3"),      
    ]
    curves_dct["unlevered_triangle"] = curves


    # ##### Unlevered square

    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ2(pair="WETH/DAI", p=3000, k=3000*vol**2, fee=0, cid="1.3.1"),  

        # curve buys/sells DAI @ 1 USDT
        CPC.from_univ2(pair="DAI/USDC", p=1, k=3000**2 * vol**2, fee=0, cid="1.3.2"),  
        
        # curve buys/sells USDT @ 1 USDC
        CPC.from_univ2(pair="DAI/USDC", p=1, k=3000**2 * vol**2, fee=0, cid="1.3.3"),  
        
        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ2(pair="WETH/USDC", p=3500, k=3500*vol**2, fee=0, cid="1.3.4"),          
    ]
    curves_dct["unlevered_square"] = curves

    # #### Levered symmetric curves

    # ##### Levered pair (narrow)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-0.1, uniPb=3000+0.1, fee=0, cid="2.1.1"),  
        
        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-0.1, uniPb=3500+0.1, fee=0, cid="2.1.2"),  
        
    ]
    curves_dct["levered_pair_narrow"] = curves
    # -

    # ##### Levered triangle (narrow)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ3(pair="WETH/DAI", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-0.1, uniPb=3000+0.1, fee=0, cid="2.2.1"),  

        # curve buys/sells DAI @ 3500 USDC
        CPC.from_univ3(pair="DAI/USDC", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.2.2"),  

        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-0.1, uniPb=3500+0.1, fee=0, cid="2.2.3"),  
        
    ]
    curves_dct["levered_triangle_narrow"] = curves
    # -

    # ##### Levered square (narrow)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ3(pair="WETH/DAI", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-0.1, uniPb=3000+0.1, fee=0, cid="2.3.1"),  

        # curve buys/sells DAI @ 3500 USDT
        CPC.from_univ3(pair="DAI/USDT", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.3.2"),  

        # curve buys/sells USDT @ 3500 USDC
        CPC.from_univ3(pair="USDT/USDC", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.3.3"),  

        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-0.1, uniPb=3500+0.1, fee=0, cid="2.3.4"),  
        
    ]
    curves_dct["levered_square_narrow"] = curves
    # -

    # ##### Levered pair (elastic)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-500, uniPb=3000+500, fee=0, cid="2.4.1"),  
        
        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-500, uniPb=3500+500, fee=0, cid="2.4.2"),  
        
    ]
    curves_dct["levered_pair_elastic"] = curves
    # -

    # ##### Levered triangle (elastic)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ3(pair="WETH/DAI", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-500, uniPb=3000+500, fee=0, cid="2.5.1"),  

        # curve buys/sells DAI @ 3500 USDC
        CPC.from_univ3(pair="DAI/USDC", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.5.2"),  

        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-500, uniPb=3500+500, fee=0, cid="2.5.3"),  
        
    ]
    curves_dct["levered_triangle_elastic"] = curves
    # -

    # ##### Levered square (elastic)

    # +
    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 DAI
        CPC.from_univ3(pair="WETH/DAI", Pmarg=3000, uniL=3000*vol**2, uniPa=3000-500, uniPb=3000+500, fee=0, cid="2.6.1"),  

        # curve buys/sells DAI @ 3500 USDT
        CPC.from_univ3(pair="DAI/USDT", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.6.2"),  

        # curve buys/sells USDT @ 3500 USDC
        CPC.from_univ3(pair="USDT/USDC", Pmarg=1, uniL=3000**2 * vol**2, uniPa=1-0.001, uniPb=1+0.001, fee=0, cid="2.6.3"),  

        # curve buys/sells WETH @ 3500 USDC
        CPC.from_univ3(pair="WETH/USDC", Pmarg=3500, uniL=3000*vol**2, uniPa=3500-500, uniPb=3500+500, fee=0, cid="2.6.4"),  
        
    ]
    curves_dct["levered_square_elastic"] = curves
    # -
    # #### Carbon curves

    # ##### Carbon pair (narrow)

    # +
    curves = [
        
        # curve buys WETH @ 3500
        CPC.from_carbonv1(pair="WETH/USDC", tkny="USDC", y=30_000, isdydx=False, pa=3501, pb=3500, cid="3.1.1"),  

        # curve sells WETH @ 3000
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10,     isdydx=False, pa=3000, pb=3001, cid="3.1.2"),
        
    ]
    curves_dct["carbon_pair_narrow"] = curves
    # -

    # ##### Carbon pair (elastic)

    curves = [
        
        # curve buys WETH @ 3500-2500 USDC
        CPC.from_carbonv1(pair="WETH/USDC", tkny="USDC", y=30_000, isdydx=False, pa=3500, pb=2500, cid="3.2.1"),  

        # curve buys USDC @ 1/3000-1/4000 WETH
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10,     isdydx=False, pa=3000, pb=4000, cid="3.2.2"),
    ]
    curves_dct["carbon_pair_elastic"] = curves

    # ##### Carbon + unlevered pair

    vol = 75
    curves = [
        
        # curve buys/sells WETH @ 3000 USDC
        CPC.from_univ2(pair="WETH/USDC", p=3000, k=3000*vol**2, fee=0, cid="3.3.1"),  

        # curve sells WETH @ 3500-2500 USDC
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10, isdydx=False, pb=3500, pa=2500, cid="3.3.2"),  
    ]
    curves_dct["carbon_pair_vsunlevered"] = curves


    # ##### Carbon triangle (narrow)

    # +
    curves = [

        # curve buys WETH @ 3500 DAI
        CPC.from_carbonv1(pair="WETH/DAI", tkny="DAI", y=50_000, isdydx=False, pa=3501, pb=3500, cid="3.4.1"),  

        # curve buys DAI @ 1 USDC
        CPC.from_carbonv1(pair="USDC/DAI", tkny="USDC", yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.4.2"),
        
        # curve buys USDC @ 1/3000 WETH
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10, isdydx=False, pa=3000, pb=3001, cid="3.4.3"),

    ]
    curves_dct["carbon_triangle_narrow"] = curves
    # -

    # ##### Carbon triangle (elastic)

    # +
    curves = [
        
        # curve buys WETH @ 3500 DAI
        CPC.from_carbonv1(pair="WETH/DAI", tkny="DAI", y=50_000, isdydx=False, pa=3501, pb=3500, cid="3.4.1"),  

        # curve buys DAI @ 1 USDC
        CPC.from_carbonv1(pair="USDC/DAI", tkny="USDC", yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.4.2"),
        
        # curve buys USDC @ 1/3000 WETH
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10, isdydx=False, pa=3000, pb=3001, cid="3.4.3"),

    ]
    curves_dct["carbon_triangle_elastic_wrong"] = curves
    # -

    # ##### Carbon square (narrow)

    # +
    curves = [
        
        # curve buys WETH @ 3500 USDT
        CPC.from_carbonv1(pair="WETH/USDT", tkny="USDT", y=50_000, isdydx=False, pa=3501, pb=3500, cid="3.5.1"),  

        # curve buys USDT @ 1 DAI
        CPC.from_carbonv1(pair="DAI/USDT", tkny="DAI",  yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.5.2"),

        # curve buys DAI @ 1 USDC
        CPC.from_carbonv1(pair="USDC/DAI", tkny="USDC", yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.5.3"),

        # curve sells USDC @ 1/3000 WETH
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10, isdydx=False, pa=3000, pb=3001, cid="3.5.4"),
        
    ]
    curves_dct["carbon_square_narrow"] = curves
    # -

    # ##### Carbon square (elastic)

    # +
    curves = [
        # curve buys WETH @ 3500-2500 USDT
        CPC.from_carbonv1(pair="WETH/USDT", tkny="USDT", y=50_000, isdydx=False, pa=3500, pb=2500, cid="3.6.1"),  

        # curve buys USDT @ 1 DAI
        CPC.from_carbonv1(pair="DAI/USDT", tkny="DAI",  yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.6.2"),

        # curve buys DAI @ 1 USDC
        CPC.from_carbonv1(pair="USDC/DAI", tkny="USDC", yint= 1_000_000, y=500_000, isdydx=False, pa=0.9999, pb=1.0001, cid="3.6.3"),

        # curve buys USDC @ 1/3000-1/4000 WETH
        CPC.from_carbonv1(pair="WETH/USDC", tkny="WETH", y=10, isdydx=False, pa=3000, pb=4000, cid="3.6.4"),

    ]
    curves_dct["carbon_square_elastic"] = curves
    # -
    
    
    # #### Return
    
    return curves_dct


        

