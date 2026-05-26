# Venture 001 — Stable Plate Planner

## Decision

This is the first zero-dollar venture because it can be built, published, and tested without inventory, ads, paid APIs, paid hosting, or payment processing.

## Product

A free static low-glycemic meal planning tool for people who want:

- high-protein meal ideas
- low-glycemic structure
- simple grocery lists
- no login
- no medical complexity

## Monetization path

Start free, then convert through Gumroad:

1. Free tool attracts users.
2. Visitors buy the $19 Custom Stable Plate Plan on Gumroad.
3. Buyer receives intake instructions after checkout.
4. Deliver plans manually through email/DM/PDF within 48–72 hours after intake is received.
5. Use customer feedback to decide whether to add more tiers, printable digital products, or affiliate links later.

Current first offer:

- **$19 custom 7-day stable plate plan** — https://harmonious54.gumroad.com/l/stable-plate-plan

Future offers to test:

- **$9 custom 3-day stable plate plan**
- **$39 monthly refresh**

No paid tools are required to begin. GitHub Pages hosts the free tool and Gumroad handles checkout: https://harmonious54.gumroad.com/l/stable-plate-plan

## Free deployment options

- GitHub Pages
- Cloudflare Pages free tier
- Netlify free tier
- Vercel free tier

## Safety boundary

This is educational meal planning support only. It is not medical advice, insulin dosing advice, diagnosis, or emergency guidance.

## Next build improvements

- Add 30 more meals.
- Add printable PDF grocery list.
- Add email capture once a free provider is chosen.
- Add affiliate links only after trust and traffic exist.
- Add SEO articles: "low glycemic high protein breakfast", "diabetic friendly chicken bowls", "stable blood sugar grocery list".

## Launch checklist

- [ ] Choose deployment host.
- [ ] Publish `index.html`.
- [ ] Add contact method.
- [ ] Share in 3 relevant communities without spam.
- [ ] Ask first 5 users what meals they actually need.
- [ ] Convert feedback into the first paid custom-plan offer.

## Zero-dollar venture framework

This repository is now the template for weekly $0 upfront ventures:

- Static free artifact first.
- Blog/content spine for SEO.
- `sitemap.xml` and `robots.txt` for discovery.
- Manual paid offer before complex automation.
- Free GitHub Actions automation where useful.

See `framework/zero-dollar-venture-framework.md`.

## Daily content engine

The blog lives in `blog/`. A free GitHub Actions workflow runs daily and uses `scripts/generate_daily_blog.py` to add one practical stable-plate SEO post, then rebuilds the blog index and sitemap.
