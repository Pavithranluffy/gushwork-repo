import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

app_start = html.find('        <!-- Product Carousel Section -->')
faq_start = html.find('        <!-- FAQ Section -->')

if app_start != -1 and faq_start != -1:
    old_app = html[app_start:faq_start]
    
    new_app = """        <!-- Product Carousel Section -->
        <section class="applications-section" style="background-color: #fcfcfc; background-image: radial-gradient(#d1d5db 1px, transparent 1px); background-size: 20px 20px; padding: 100px 0;">
            <div class="container container-app" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
                <div class="app-header" style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 60px;">
                    <div class="app-text" style="max-width: 650px;">
                        <h2 style="font-size: 2.75rem; font-weight: 700; color: #111827; line-height: 1.2; margin-bottom: 16px;">Versatile Applications Across<br>Industries</h2>
                        <p style="color: #6b7280; font-size: 1.1rem; line-height: 1.6;">From technical textiles to packaging materials, our precision-engineered<br>machinery delivers superior performance across diverse applications.</p>
                    </div>
                    <div class="app-controls" style="display: flex; gap: 16px;">
                        <button class="nav-btn prev-app styled-nav-btn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                        </button>
                        <button class="nav-btn next-app styled-nav-btn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </button>
                    </div>
                </div>

                <div class="applications-carousel-container" style="overflow: hidden; padding-bottom: 20px;">
                    <div class="applications-carousel" id="appCarousel" style="display: flex; gap: 32px; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; padding-right: 20px;">
                        <div class="app-card styled-app-card">
                            <img src="https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=400" alt="App">
                            <div class="app-card-content styled-app-content">
                                <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">Fishnet Manufacturing</h3>
                                <p style="font-size: 0.95rem; color: #d1d5db; line-height: 1.5;">High-performance twisting solutions for packaging yarn, strapping materials, and reinforcement threads used in modern packaging applications.</p>
                            </div>
                        </div>
                        <div class="app-card styled-app-card">
                            <img src="https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=400" alt="App">
                            <div class="app-card-content styled-app-content">
                                <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">Fishnet Manufacturing</h3>
                                <p style="font-size: 0.95rem; color: #d1d5db; line-height: 1.5;">High-performance twisting solutions for packaging yarn, strapping materials, and reinforcement threads used in modern packaging applications.</p>
                            </div>
                        </div>
                        <div class="app-card styled-app-card">
                            <img src="https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=400" alt="App">
                            <div class="app-card-content styled-app-content">
                                <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">Fishnet Manufacturing</h3>
                                <p style="font-size: 0.95rem; color: #d1d5db; line-height: 1.5;">High-performance twisting solutions for packaging yarn, strapping materials, and reinforcement threads used in modern packaging applications.</p>
                            </div>
                        </div>
                        <div class="app-card styled-app-card">
                            <img src="https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=400" alt="App">
                            <div class="app-card-content styled-app-content">
                                <h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 12px;">Fishnet Manufacturing</h3>
                                <p style="font-size: 0.95rem; color: #d1d5db; line-height: 1.5;">High-performance twisting solutions for packaging yarn, strapping materials, and reinforcement threads used in modern packaging applications.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

"""
    result = html.replace(old_app, new_app)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
        print("Success updating Applications Carousel")
else:
    print("Could not find section markers")
