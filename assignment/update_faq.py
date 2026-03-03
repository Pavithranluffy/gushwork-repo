import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_start = html.find('        <!-- FAQ Section -->')
end_main = html.find('    </main>')

if faq_start != -1 and end_main != -1:
    old_faq = html[faq_start:end_main]
    
    new_faq = """        <!-- FAQ Section -->
        <section class="faq-section" style="background-color: #f9fafb; background-image: radial-gradient(#d1d5db 1px, transparent 1px); background-size: 20px 20px; padding: 100px 0;">
            <div class="container container-faq">
                <div class="section-header align-left" style="margin-bottom: 48px;">
                    <h2 style="font-size: 2.5rem; font-weight: 700; color: #111827; margin-bottom: 16px;"><span style="color: #2b3d86;">Frequently</span> Asked Questions</h2>
                </div>

                <div class="faq-list" style="display: flex; flex-direction: column; gap: 16px;">
                    <div class="faq-item active" style="border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div class="faq-question" style="padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 500; font-size: 1.05rem; color: #111827;">
                            <span>What is the purpose of a laser cutter for sheet metal?</span>
                            <span class="icon" style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #fdf2f8; color: #db2777; flex-shrink: 0; margin-left: 16px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer" style="padding: 0 24px 24px; color: #6b7280; font-size: 0.95rem; line-height: 1.6;">
                            It is designed to cut various types of sheet metal with precision, allowing for intricate
                            designs and shapes that are essential in manufacturing processes.
                        </div>
                    </div>
                    
                    <div class="faq-item" style="border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div class="faq-question" style="padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 500; font-size: 1.05rem; color: #111827;">
                            <span>What are the benefits of using aluminum tubing in manufacturing?</span>
                            <span class="icon" style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #f3f4f6; color: #6b7280; flex-shrink: 0; margin-left: 16px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer" style="padding: 0 24px 24px; color: #6b7280; font-size: 0.95rem; line-height: 1.6; display: none;">
                            Aluminum tubing is lightweight, corrosion-resistant, and offers an excellent
                            strength-to-weight ratio.
                        </div>
                    </div>
                    
                    <div class="faq-item" style="border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div class="faq-question" style="padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 500; font-size: 1.05rem; color: #111827;">
                            <span>How is aluminum tubing produced?</span>
                            <span class="icon" style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #f3f4f6; color: #6b7280; flex-shrink: 0; margin-left: 16px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer" style="padding: 0 24px 24px; color: #6b7280; font-size: 0.95rem; line-height: 1.6; display: none;">
                            It is primarily produced through an extrusion process where a heated aluminum billet is
                            forced through a die.
                        </div>
                    </div>
                    
                    <div class="faq-item" style="border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div class="faq-question" style="padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 500; font-size: 1.05rem; color: #111827;">
                            <span>What are the common applications of aluminum tubing?</span>
                            <span class="icon" style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #f3f4f6; color: #6b7280; flex-shrink: 0; margin-left: 16px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer" style="padding: 0 24px 24px; color: #6b7280; font-size: 0.95rem; line-height: 1.6; display: none;">
                            Common applications include aerospace components, automotive parts, structural frames, and
                            pneumatic cylinders.
                        </div>
                    </div>
                    
                    <div class="faq-item" style="border: 1px solid #e5e7eb; border-radius: 8px; background: #fff; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div class="faq-question" style="padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 500; font-size: 1.05rem; color: #111827;">
                            <span>Can aluminum tubing be customized?</span>
                            <span class="icon" style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #f3f4f6; color: #6b7280; flex-shrink: 0; margin-left: 16px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer" style="padding: 0 24px 24px; color: #6b7280; font-size: 0.95rem; line-height: 1.6; display: none;">
                            Yes, it can be customized in terms of length, diameter, wall thickness, and alloy
                            composition.
                        </div>
                    </div>
                </div>

                <div class="catalogue-box" style="margin-top: 60px; background: #fcfcfc; border: 1px solid #e5e7eb; padding: 40px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; gap: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
                    <div class="catalogue-text" style="flex: 1;">
                        <h3 style="font-size: 1.5rem; color: #111827; font-weight: 600; margin-bottom: 8px;">Want us to email the entire catalogue?</h3>
                        <p style="color: #6b7280; font-size: 0.95rem;">Enter your email and an expert will share the catalogue with you.</p>
                    </div>
                    <div class="catalogue-form" style="display: flex; gap: 16px; flex: 1; justify-content: flex-end;">
                        <input type="email" placeholder="Email Address" style="padding: 12px 16px; border: 1px solid #e5e7eb; border-radius: 6px; flex: 1; max-width: 300px; outline: none; background: #fff;">
                        <button class="btn btn-primary" onclick="openModal('quoteModal')" style="background-color: #2b3d86; border-radius: 6px; padding: 12px 24px; font-weight: 500; white-space: nowrap;">Request Catalogue</button>
                    </div>
                </div>
            </div>
        </section>
"""
    result = html.replace(old_faq, new_faq)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
        print("Success updating FAQ")
else:
    print("Could not find section markers")
