#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import hashlib, json, re
ROOT = Path(__file__).resolve().parents[1]
BASE = "https://bkhjr1297.github.io/stable-plate-planner"
POSTS = ROOT / "blog" / "posts"
POSTS.mkdir(parents=True, exist_ok=True)
TOPICS = [
("high-protein low-glycemic breakfast bowl", "High-Protein Low-Glycemic Breakfast Bowl", "A simple breakfast bowl formula for steadier morning energy."),
("low-glycemic chicken dinner", "Low-Glycemic Chicken Dinner Formula", "A repeatable chicken dinner plate built around protein, fiber, and slow carbs."),
("diabetic friendly grocery list", "Diabetic-Friendly Grocery List Basics", "A conservative educational grocery framework for lower-sugar meal planning."),
("stable blood sugar snacks", "Stable Blood Sugar Snack Ideas", "Snack combinations that pair protein, fiber, and deliberate carbs."),
("low-glycemic meal prep", "Low-Glycemic Meal Prep for Busy Weeks", "A low-stress meal prep rhythm using repeatable anchor foods."),
("budget high protein meals", "Budget High-Protein Meals for Stable Energy", "Low-cost protein and fiber pairings for practical weekly planning."),
("low sugar lunch ideas", "Low-Sugar Lunch Ideas That Still Feel Filling", "Lunch ideas that reduce hidden sugar without becoming complicated."),
("slow carb grocery staples", "Slow-Carb Grocery Staples for Stable Plates", "A practical pantry list for slow-carb meal building."),
("no cook low-glycemic meals", "No-Cook Low-Glycemic Meal Ideas", "Fast stable plate combinations for low-energy days."),
("high fiber low-glycemic foods", "High-Fiber Low-Glycemic Foods to Keep on Hand", "Fiber-forward foods that make stable plates easier to assemble."),
("low-glycemic meal planning for beginners", "Low-Glycemic Meal Planning for Beginners", "A beginner-friendly way to build stable plates without tracking everything."),
("protein fiber slow carb plate", "The Protein + Fiber + Slow Carb Plate", "The core Stable Plate Planner method in one repeatable formula."),
]
def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
def article(topic, title, desc, today):
    slug = f"{slugify(title)}-{today}"
    return f"""<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>{title} | Stable Plate Blog</title><meta name=\"description\" content=\"{desc}\"><link rel=\"canonical\" href=\"{BASE}/blog/posts/{slug}.html\"><meta name=\"robots\" content=\"index, follow\"><link rel=\"stylesheet\" href=\"../style.css\"><script type=\"application/ld+json\">{{\"@context\":\"https://schema.org\",\"@type\":\"BlogPosting\",\"headline\":{json.dumps(title)},\"description\":{json.dumps(desc)},\"datePublished\":\"{today}\",\"author\":{{\"@type\":\"Organization\",\"name\":\"Stable Plate Planner\"}},\"mainEntityOfPage\":\"{BASE}/blog/posts/{slug}.html\"}}</script></head><body><header><div class=\"wrap\"><nav><a class=\"brand\" href=\"../../\">Stable Plate Planner</a><div class=\"links\"><a href=\"../\">Blog</a><a href=\"../../#planner\">Planner</a><a href=\"https://harmonious54.gumroad.com/l/stable-plate-plan\">Custom Plan</a></div></nav></div></header><main><article class=\"wrap\"><div class=\"eyebrow\">Daily stable-energy guide</div><h1>{title}</h1><p class=\"post-meta\">Published {today} - Target keyword: {topic}</p><p class=\"muted\">{desc}</p><h2>Use the stable plate formula</h2><p>Build the meal around one protein anchor, at least one fiber-rich food, and a deliberate slow-carb choice if the meal needs it. This keeps the plan useful without turning every meal into a complicated nutrition project.</p><h2>Simple examples</h2><p>Good combinations include eggs with greens and avocado, chicken with salad and beans, Greek yogurt with chia and berries, tuna lettuce wraps with lentil soup, or tofu with frozen vegetables and cauliflower rice.</p><h2>Grocery list starter</h2><p>Keep eggs, plain Greek yogurt, chicken, tuna, tofu, beans, lentils, greens, broccoli, cucumbers, berries, chia, flax, olive oil, and sweet potatoes available when budget allows.</p><h2>Make it easier tomorrow</h2><p>Pick one repeatable breakfast, one emergency snack, and one dinner bowl. Repetition is an advantage when the goal is stable energy and low decision stress.</p><div class=\"warning\">Educational planning support only. This is not medical advice, diagnosis, medication, or insulin dosing guidance. Follow your clinician's plan for diabetes care and urgent situations.</div><p><a class=\"btn\" href=\"../../#planner\">Try the free meal planner</a> <a class=\"btn secondary\" href=\"https://harmonious54.gumroad.com/l/stable-plate-plan\">Buy a $19 custom plan</a></p></article></main><footer><div class=\"wrap\">© 2026 Stable Plate Planner</div></footer></body></html>"""
def rebuild_indexes():
    files=sorted(POSTS.glob('*.html'), reverse=True)
    cards=[]; urls=[f"{BASE}/", f"{BASE}/blog/"]
    for f in files:
        txt=f.read_text()
        title=re.search(r"<h1>(.*?)</h1>", txt, re.S)
        desc=re.search(r'<meta name="description" content="(.*?)"', txt)
        meta=re.search(r'<p class="post-meta">(.*?)</p>', txt)
        title=title.group(1) if title else f.stem
        desc=desc.group(1) if desc else "Stable Plate Blog post."
        meta=meta.group(1) if meta else "Daily guide"
        cards.append(f'<article class="card"><h2><a href="posts/{f.name}">{title}</a></h2><p class="post-meta">{meta}</p><p class="muted">{desc}</p></article>')
        urls.append(f"{BASE}/blog/posts/{f.name}")
    (ROOT/'blog/index.html').write_text(f"""<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Stable Plate Blog — Low-Glycemic Meal Planning Guides</title><meta name=\"description\" content=\"Daily low-glycemic meal planning guides, high-protein plate ideas, grocery lists, and stable-energy routines.\"><link rel=\"canonical\" href=\"{BASE}/blog/\"><meta name=\"robots\" content=\"index, follow\"><link rel=\"stylesheet\" href=\"style.css\"></head><body><header><div class=\"wrap\"><nav><a class=\"brand\" href=\"../\">Stable Plate Planner</a><div class=\"links\"><a href=\"../#planner\">Planner</a><a href=\"../#contact\">Custom Plan</a><a href=\"https://harmonious54.gumroad.com/l/stable-plate-plan\">Buy</a></div></nav></div></header><main class=\"wrap\"><div class=\"eyebrow\">Daily content</div><h1>Stable Plate Blog</h1><p class=\"muted\">Search-friendly, practical guides for low-glycemic meals, high-protein plates, simple grocery lists, and steady energy.</p><section class=\"post-list\">{''.join(cards)}</section></main><footer><div class=\"wrap\">Educational planning support only, not medical advice.</div></footer></body></html>""")
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(f'  <url><loc>{u}</loc><changefreq>{"daily" if "/blog" in u else "weekly"}</changefreq><priority>{"0.8" if "/blog" in u else "1.0"}</priority></url>' for u in urls)+'\n</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sm)
def main():
    today=date.today().isoformat()
    idx=int(hashlib.sha256(today.encode()).hexdigest(),16) % len(TOPICS)
    topic,title,desc=TOPICS[idx]
    filename=f"{slugify(title)}-{today}.html"
    path=POSTS/filename
    if not path.exists():
        path.write_text(article(topic,title,desc,today))
    rebuild_indexes()
if __name__ == '__main__': main()
