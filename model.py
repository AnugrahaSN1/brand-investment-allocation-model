"""Illustrative model: where should an extra brand-investment budget go across L'Oreal's four divisions?
Division sales and growth are from the H1 2026 press release (annualised x2). Response curves, gross margin and
carry-over are ASSUMPTIONS, not L'Oreal data."""
import json, math
DIV=[("Dermatological Beauty",4215.8,11.3),("Professional Products",2920.8,12.6),("L'Oreal Luxe",7996.7,5.4),("Consumer Products",8642.8,4.1)]
BUDGET=330.0     # EUR m, ~70 bp of annualised group sales (assumption: H1 increase repeated over a year)
ROI0=1.0         # first-euro return (incremental annual sales per EUR) for a division growing at the group rate 6.8%
GROUP_LFL=6.8
SAT=0.015        # spend at which a division is ~63% saturated, as share of its annual sales
GM=0.74          # gross margin on incremental sales (assumption)
CARRY=0.60       # share of the sales effect that persists each following year (long-term brand effect)
def setup(alike=False,roi0=ROI0,sat=SAT):
    out=[]
    for n,h1,g in DIV:
        S=2*h1; r=roi0 if alike else roi0*g/GROUP_LFL; K=sat*S
        if alike: K=sat*(sum(2*d[1] for d in DIV)/len(DIV))   # same absolute curve for everyone
        out.append(dict(name=n,S=S,g=g,r=r,K=K))
    return out
def gain(d,x): return d["r"]*d["K"]*(1-math.exp(-x/d["K"]))
def optimal(divs,B):
    lo,hi=0.0,max(d["r"] for d in divs)   # lambda = marginal return per EUR
    for _ in range(200):
        lam=(lo+hi)/2
        x=[max(0.0,d["K"]*math.log(d["r"]/lam)) if d["r"]>lam else 0.0 for d in divs]
        if sum(x)>B: lo=lam
        else: hi=lam
    return x
def evaluate(divs,x,years=3):
    inc=[gain(d,xi) for d,xi in zip(divs,x)]; tot=sum(inc); S=sum(d["S"] for d in divs)
    y1=tot*GM-sum(x); cum=sum(tot*GM*CARRY**t for t in range(years))-sum(x)
    return dict(x=x,inc=inc,sales=tot,growth_pts=tot/S*100,y1_profit=y1,cum_profit=cum,
                payback_ratio=sum(tot*GM*CARRY**t for t in range(years))/sum(x))
def run(alike=False,B=BUDGET,**kw):
    divs=setup(alike,**kw); S=sum(d["S"] for d in divs)
    pro=[B*d["S"]/S for d in divs]; foc=optimal(divs,B)
    P,F=evaluate(divs,pro),evaluate(divs,foc)
    return dict(pro=P,foc=F,ratio=F["sales"]/P["sales"],divs=divs)
if __name__=="__main__":
    R=run(); A=run(alike=True)
    res={"budget":BUDGET,"ratio":R["ratio"],"ratio_alike":A["ratio"],
         "pro":{k:R["pro"][k] for k in("growth_pts","sales","y1_profit","cum_profit","payback_ratio","x")},
         "foc":{k:R["foc"][k] for k in("growth_pts","sales","y1_profit","cum_profit","payback_ratio","x")},
         "alike":{k:A["foc"][k] for k in("growth_pts","x")},"alike_pro_growth":A["pro"]["growth_pts"]}
    sens={}
    for lab,kw in (("ROI0 0.6",dict(roi0=0.6)),("ROI0 1.4",dict(roi0=1.4)),("SAT 0.8%",dict(sat=0.008)),("SAT 3%",dict(sat=0.03))):
        sens[lab]=round(run(**kw)["ratio"],2)
    res["sens"]=sens
    res["budget_curve"]={b:round(run(B=b)["ratio"],2) for b in (110,220,330,440,660)}
    json.dump(res,open("results.json","w"),indent=1); print(json.dumps(res,indent=1))
