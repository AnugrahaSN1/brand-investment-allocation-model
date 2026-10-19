Brand Investment Allocation Model

If a beauty group raises brand investment, does it matter where the extra money goes? This model compares two ways of spending an extra EUR 330M across four divisions: a pro rata split (in proportion to sales) and a focused split (the best response per euro).

Independent student project using publicly available results. Not affiliated with or endorsed by L'Oréal. The response curves are illustrative assumptions, not company data, and the results are not a forecast.

Show Image

What it does
Starts from L'Oréal's published H1 2026 sales and like-for-like growth by division (annualised x2): Dermatological Beauty, Professional Products, L'Oréal Luxe, Consumer Products.
Models each division with a diminishing-returns curve: the first euro earns more in faster-growing divisions, and the return falls as spend rises.
Finds the focused split by equalising the marginal return of every division.
Compares growth, year-one profit and a three-year view (with a persistence effect on sales).
Lets you change the budget and every assumption in the dashboard and see the result move.
Results under the default assumptions
	Pro rata	Focused
Extra growth (points of group sales)	0.56	0.65
Year-one profit after the spend (EUR m)	-133	-100
Three-year cumulative profit (EUR m)	+56	+121

Focusing the same budget gives about 1.17x the incremental sales of a pro rata split. The advantage depends on the assumptions: it falls to about 1.07x when saturation is 0.8% of division sales and rises to about 1.35x at 3%. It is larger for a smaller budget (about 1.46x at EUR 110M) and smaller for a larger one (about 1.06x at EUR 660M). If every division responds identically, there is almost no advantage (about 1.03x).

Run it

Dashboard: open index.html in a browser. It has no dependencies. If you publish the repo with GitHub Pages, it also works as a live link.

Script: python model.py (Python 3, standard library only). It prints the results and writes results.json.

Assumptions (all editable)
Assumption	Default
Extra budget	EUR 330M (about 70 bp of annualised group sales)
First-euro return	1.0 sales per EUR at the group growth rate of 6.8%, scaled by each division's growth
Saturation	1.5% of a division's annual sales
Gross margin on incremental sales	74%
Persistence of the sales effect each following year	60%
Files
model.py: the model and sensitivity analysis.
index.html: the interactive dashboard.
docs/memo.pdf: a short written summary of the approach and findings.
Author

Anugraha SN, EDHEC Business School (BBA, Data Analytics). Open to a 6-month internship from January 2027. LinkedIn
