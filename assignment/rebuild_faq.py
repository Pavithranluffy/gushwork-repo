import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_start = html.find('        <!-- FAQ Section -->')
catalogue_start = html.find('                <div class="catalogue-box"')

if faq_start != -1 and catalogue_start != -1:
    old_faq_top = html[faq_start:catalogue_start]
    
    new_faq_top = """        <!-- FAQ Section -->
        <section class="faq-section" style="background-color: #f9fafb; background-image: radial-gradient(#d1d5db 1px, transparent 1px); background-size: 20px 20px; padding: 100px 0;">
            <div class="container container-faq">
                <div class="section-header align-left" style="margin-bottom: 48px;">
                    <h2 style="font-size: 2.5rem; font-weight: 700; color: #111827; margin-bottom: 16px;"><span style="color: #2b3d86;">Frequently</span> Asked Questions</h2>
                </div>

                <div class="faq-list" style="display: flex; flex-direction: column; gap: 16px;">
                    <div class="faq-item styled-faq active">
                        <div class="faq-question">
                            <span>What is the purpose of a laser cutter for sheet metal?</span>
                            <span class="icon styled-faq-icon">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="faq-chevron" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer-wrapper">
                            <div class="faq-answer">
                                It is designed to cut various types of sheet metal with precision, allowing for intricate
                                designs and shapes that are essential in manufacturing processes.
                            </div>
                        </div>
                    </div>
                    
                    <div class="faq-item styled-faq">
                        <div class="faq-question">
                            <span>What are the benefits of using aluminum tubing in manufacturing?</span>
                            <span class="icon styled-faq-icon">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="faq-chevron" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer-wrapper">
                            <div class="faq-answer">
                                Aluminum tubing is lightweight, corrosion-resistant, and offers an excellent
                                strength-to-weight ratio.
                            </div>
                        </div>
                    </div>
                    
                    <div class="faq-item styled-faq">
                        <div class="faq-question">
                            <span>How is aluminum tubing produced?</span>
                            <span class="icon styled-faq-icon">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="faq-chevron" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer-wrapper">
                            <div class="faq-answer">
                                It is primarily produced through an extrusion process where a heated aluminum billet is
                                forced through a die.
                            </div>
                        </div>
                    </div>
                    
                    <div class="faq-item styled-faq">
                        <div class="faq-question">
                            <span>What are the common applications of aluminum tubing?</span>
                            <span class="icon styled-faq-icon">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="faq-chevron" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer-wrapper">
                            <div class="faq-answer">
                                Common applications include aerospace components, automotive parts, structural frames, and
                                pneumatic cylinders.
                            </div>
                        </div>
                    </div>
                    
                    <div class="faq-item styled-faq">
                        <div class="faq-question">
                            <span>Can aluminum tubing be customized?</span>
                            <span class="icon styled-faq-icon">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="faq-chevron" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </span>
                        </div>
                        <div class="faq-answer-wrapper">
                            <div class="faq-answer">
                                Yes, it can be customized in terms of length, diameter, wall thickness, and alloy
                                composition.
                            </div>
                        </div>
                    </div>
                </div>

"""
    result = html.replace(old_faq_top, new_faq_top)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
        print("Success updating FAQ HTML")
else:
    print("Could not find section markers")
