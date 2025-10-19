Website improvement suggestions

## 🎯 **PRIORITY 1: Wine Collection Section (Critical for Export)**

**PROMPT FOR AGENT:**

```
Add a new section titled "OUR COLLECTION" after the story section. Create two wine cards with the following exact content and styling to match the site's burgundy/gold theme:
```

**CONTENT TO ADD:**

```html
<section class="wine-collection">
  <h2>Our Collection</h2>
  
  <div class="wine-grid">
    <div class="wine-card saperavi">
      <div class="wine-image">
        <!-- Add bottle image here -->
      </div>
      <h3>Alaverdi Saperavi 1782</h3>
      <p class="wine-type">Reserve Red | 100% Saperavi | ABV: 13.5–14% | 750ml</p>
      
      <div class="tasting-notes">
        <h4>Tasting Notes</h4>
        <p>Deep ruby-garnet color. Aromas of black cherry, plum and graphite. Rich, structured palate with elegant tannin, cedar spice and a long mineral finish. Oak-aged 12–18 months.</p>
      </div>
      
      <div class="pairing">
        <h4>Perfect Pairings</h4>
        <p>Roasted lamb, aged cheeses, and dark chocolate desserts.</p>
      </div>
    </div>

    <div class="wine-card rkatsiteli">
      <div class="wine-image">
        <!-- Add bottle image here -->
      </div>
      <h3>Alaverdi Rkatsiteli 1782</h3>
      <p class="wine-type">Classic White | 100% Rkatsiteli | ABV: 12.5–13% | 750ml</p>
      
      <div class="tasting-notes">
        <h4>Tasting Notes</h4>
        <p>Golden amber hue. Fragrant notes of pear, quince, and wild honey. Textured, layered, and elegant with vibrant acidity. Long, savoury finish.</p>
      </div>
      
      <div class="pairing">
        <h4>Perfect Pairings</h4>
        <p>Grilled fish, spice-forward vegetable dishes, and light poultry.</p>
      </div>
    </div>
  </div>
</section>
```

## 🎯 **PRIORITY 2: Enhanced Story Section Language**

**PROMPT FOR AGENT:**

```
Find and replace the existing story text with these refined versions. Keep the same structure but upgrade the language for premium positioning:
```

**SPECIFIC REPLACEMENTS:**

```
REPLACE: "Named in homage to the restoration year of the sacred Alaverdi Monastery"
WITH: "Named in honor of the sacred Alaverdi Monastery's restoration in 1782"

REPLACE: "each bottle expresses the land, the light, and the centuries of devotion that define Georgian wine"  
WITH: "each bottle captures the terroir, the Georgian sunlight, and eight millennia of winemaking devotion"

ADD AFTER EXISTING VISION: 
"At Château Alaverdi 1782, we bridge Georgia's ancient winemaking soul with contemporary refinement. Our wines honor the qvevri tradition—UNESCO-recognized clay vessels that have shaped Georgian wine for millennia—while embracing modern techniques that elevate quality to international standards."
```

## 🎯 **PRIORITY 3: Terroir & Craft Section**

**PROMPT FOR AGENT:**

```
Add a new section called "TERROIR & CRAFT" between the story and wine collection. Use these exact specifications:
```

**CONTENT TO ADD:**

```html
<section class="terroir-craft">
  <div class="terroir-grid">
    <div class="terroir-text">
      <h2>Kakheti Terroir</h2>
      <div class="terroir-details">
        <p><strong>Region:</strong> Kakheti, Eastern Georgia</p>
        <p><strong>Vineyards:</strong> Hand-harvested grapes from family plots in the Alaverdi valley</p>
        <p><strong>Method:</strong> Ancient qvevri fermentation meets modern cellar precision</p>
        <p><strong>Philosophy:</strong> Minimal intervention. Maximum expression. Pure Georgian soul.</p>
      </div>
    </div>
    
    <div class="heritage-icons">
      <div class="heritage-item">
        <span class="icon">🍇</span>
        <h3>Ancient Terroir</h3>
        <p>Sunlit valleys and mineral-rich soils nurturing vines for millennia</p>
      </div>
      <div class="heritage-item">
        <span class="icon">🏺</span>
        <h3>Qvevri Tradition</h3>
        <p>UNESCO-recognized clay vessel fermentation, honored for 8,000 years</p>
      </div>
      <div class="heritage-item">
        <span class="icon">🏛️</span>
        <h3>Monastic Legacy</h3>
        <p>Spiritual winemaking tradition from Alaverdi Monastery since 1782</p>
      </div>
    </div>
  </div>
</section>
```

## 🎯 **PRIORITY 4: Export & Commercial Section**

**PROMPT FOR AGENT:**

```
Add a professional export section for B2B customers. Place this before the footer:
```

**CONTENT TO ADD:**

```html
<section class="export-commercial">
  <h2>For Importers & Distributors</h2>
  
  <div class="commercial-grid">
    <div class="product-specs">
      <h3>Product Information</h3>
      <ul>
        <li>Available: 750ml bottles</li>
        <li>Magnums: Available on request</li>
        <li>MOQ: 300-600 bottles</li>
        <li>Samples: Available for qualified distributors</li>
        <li>Lead time: 8-12 weeks</li>
      </ul>
    </div>
    
    <div class="markets">
      <h3>Current Markets</h3>
      <p><strong>Established:</strong> Georgia, Armenia, Russia, China</p>
      <p><strong>Expanding to:</strong> Central Asia, Middle East, Europe</p>
    </div>
    
    <div class="contact-commercial">
      <h3>Commercial Contacts</h3>
      <p><strong>Export Inquiries:</strong> <a href="mailto:export@chateaualaverdi.ge">export@chateaualaverdi.ge</a></p>
      <p><strong>Commercial:</strong> <a href="mailto:kristina@chateaualaverdi.ge">kristina@chateaualaverdi.ge</a></p>
      <p><strong>Winery Visits:</strong> By appointment</p>
    </div>
  </div>
  
  <div class="cta-buttons">
    <button class="cta-primary">Request Samples</button>
    <button class="cta-secondary">Download Wine Sheets</button>
    <button class="cta-secondary">Schedule Tasting</button>
  </div>
</section>
```

## 🎯 **PRIORITY 5: CSS Styling Instructions**

**PROMPT FOR AGENT:**

```
Add these CSS styles to maintain the burgundy/gold theme across new sections. Use the site's existing color variables:
```

**CSS TO ADD:**

```css
/* Wine Collection Styles */
.wine-collection {
  padding: 80px 20px;
  background: white;
}

.wine-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.wine-card {
  background: #f9f9f9;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.wine-card:hover {
  transform: translateY(-10px);
}

.wine-card h3 {
  color: #651f29;
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

.wine-type {
  color: #d4af37;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.pairing {
  background: #651f29;
  color: #f5f5dc;
  padding: 1rem;
  border-radius: 5px;
  margin-top: 1rem;
}

.pairing h4 {
  color: #d4af37;
}

/* Terroir & Craft Styles */
.terroir-craft {
  padding: 80px 20px;
  background: #f5f5dc;
}

.terroir-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  max-width: 1200px;
  margin: 0 auto;
}

.heritage-item {
  text-align: center;
  padding: 1.5rem;
}

.heritage-item .icon {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 1rem;
}

/* Export Section Styles */
.export-commercial {
  padding: 80px 20px;
  background: #651f29;
  color: #f5f5dc;
}

.commercial-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto 3rem;
}

.cta-buttons {
  text-align: center;
  margin-top: 3rem;
}

.cta-primary {
  background: #d4af37;
  color: #651f29;
  padding: 15px 30px;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 1rem;
  cursor: pointer;
}

.cta-secondary {
  background: transparent;
  color: #d4af37;
  border: 2px solid #d4af37;
  padding: 15px 30px;
  border-radius: 5px;
  font-size: 1.1rem;
  margin: 0 1rem;
  cursor: pointer;
}
```

## 🎯 **PRIORITY 6: SEO & Meta Improvements**

**PROMPT FOR AGENT:**

```
Update the page meta tags and add structured data for better search visibility:
```

**META TAGS TO UPDATE:**

```html
<title>Château Alaverdi 1782 - Premium Georgian Wines | Saperavi & Rkatsiteli | Export</title>
<meta name="description" content="Premium Georgian wines from Château Alaverdi 1782. Traditional qvevri Saperavi and Rkatsiteli wines from Kakheti. Export inquiries welcome.">
<meta name="keywords" content="Georgian wine, Château Alaverdi, Saperavi, Rkatsiteli, Kakheti wine, qvevri wine, wine export, premium wine">

<!-- Open Graph for social sharing -->
<meta property="og:title" content="Château Alaverdi 1782 - Premium Georgian Wines">
<meta property="og:description" content="8,000 years of Georgian winemaking heritage. Premium Saperavi and Rkatsiteli wines from Kakheti.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://chateaualaverdi.com">
```

## 📋 **IMPLEMENTATION ORDER:**

**Tell your IDE agent to implement in this sequence:**

1. Wine Collection section (highest priority for export business)
2. Enhanced story language
3. Terroir & Craft section
4. Export/Commercial section
5. CSS styling
6. SEO meta updates

**AGENT TESTING PROMPT:**

```
After each section, verify:
- Mobile responsiveness 
- Color scheme consistency (#651f29 burgundy, #d4af37 gold, #f5f5dc cream)
- Typography matches existing site
- All links work properly
- Forms function correctly
```

This gives your IDE agent everything needed to transform your site into a comprehensive, export-ready wine business website! 🍷