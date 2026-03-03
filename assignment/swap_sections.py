import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

features_start = html.find('        <!-- Features Section -->')
specs_start = html.find('        <!-- Technical Specs Table Section -->')
specs_end = html.find('        <!-- Product Carousel Section -->')

if features_start != -1 and specs_start != -1 and specs_end != -1:
    features_html = html[features_start:specs_start]
    specs_html = html[specs_start:specs_end]
    
    # New Specs Section HTML
    new_specs_html = """        <!-- Technical Specs Table Section -->
        <section class="specs-section dark-bg">
            <div class="container container-specs">
                <div class="specs-blue-dashed" style="border: 1px dashed #3168be; padding: 24px 32px; margin-bottom: 32px;">
                    <div class="section-header align-left text-white" style="margin-top:0;">
                        <h2 style="font-size: 2.25rem; font-weight: 700; margin-bottom: 8px;">Technical Specifications at a Glance</h2>
                        <p style="color: #9ca3af; max-width: 600px; font-size: 14px;">Comprehensive performance data demonstrating our commitment to quality and engineering excellence.</p>
                    </div>
                </div>

                <div class="table-container specs-table-dashed" style="border: 1px dashed #3168be; border-radius: 4px; overflow: hidden; margin-bottom: 40px;">
                    <table class="specs-table" style="width: 100%; border-collapse: collapse; margin-top: 0; background: transparent;">
                        <thead>
                            <tr>
                                <th style="background: #374151; color: #d1d5db; padding: 16px 24px; font-weight: 600; font-size: 13px; text-transform: uppercase;">PARAMETER</th>
                                <th style="background: #374151; color: #d1d5db; padding: 16px 24px; font-weight: 600; font-size: 13px; text-transform: uppercase;">SPECIFICATION</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Pipe Diameter Range</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">20mm to 1600mm (3/4" to 63")</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Pressure Ratings</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">PN 2.5, PN 4, PN 6, PN 8, PN 10, PN 12.5, PN 16</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Standard Dimension Ratio</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">SDR 33, SDR 26, SDR 21, SDR 17, SDR 13.6, SDR 11</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Operating Temperature</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">-40C to +80C (-40F to +176F)</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Service Life</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">50+ Years (at 20 degrees C, PN 10)</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Material Density</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">0.95 - 0.96 g/cm3</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Certification Standards</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">IS 5984, ISO 4427, ASTM D3035</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Joint Type</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Butt Fusion, Electrofusion, Mechanical</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Coil Lengths</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; border-bottom: 1px solid #374151; font-size: 14px;">Up to 500mm (for smaller diameters)</td>
                            </tr>
                            <tr>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; font-size: 14px;">Country of Origin</td>
                                <td style="background: #1f2937; color: #f9fafb; padding: 16px 24px; font-size: 14px;"><span style="display:inline-flex; align-items:center; gap:6px;"><img src="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg" width="16" style="border-radius:2px;"> India</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="text-center" style="display: flex; justify-content: center; margin-top: 40px;">
                    <button class="btn btn-outline-white" onclick="openModal('datasheetModal')" style="border: 1px dashed #3168be; background: #1a202c; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 14px; font-weight: 500; height: 48px; border-radius: 4px; padding: 0 40px; color: #fff;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            style="margin-right: 2px;">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        Download Full Technical Datasheet
                    </button>
                </div>
            </div>
        </section>

"""
    
    # Swap order: Specs first, then Features
    result = html[:features_start] + new_specs_html + features_html + html[specs_end:]
    
    # Update modal html
    old_modal = """    <div class="modal-overlay" id="datasheetModal">
        <div class="modal">
            <button class="close-modal" onclick="closeModal('datasheetModal')">&times;</button>
            <h2>Download Datasheet</h2>
            <p>Please enter your details to access the full technical datasheet.</p>
            <form class="modal-form" onsubmit="event.preventDefault(); closeModal('datasheetModal');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Work Email" required>
                <button type="submit" class="btn btn-primary w-100">Download PDF</button>
            </form>
        </div>
    </div>"""
    
    new_modal = """    <div class="modal-overlay" id="datasheetModal">
        <div class="modal custom-brochure-modal" style="padding: 0; max-width: 500px; border-radius: 8px; overflow: hidden; position: relative;">
            <div class="modal-header-flex" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e5e7eb; padding: 20px 24px;">
                <h2 style="font-size: 15px; font-weight: 600; margin: 0; color: #111;">Let us email the entire catalogue to you</h2>
                <button class="close-modal-icon" onclick="closeModal('datasheetModal')" style="background: transparent; border: 1px solid #e5e7eb; border-radius: 4px; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #6b7280; font-size: 16px;">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            
            <form class="brochure-form" onsubmit="event.preventDefault(); closeModal('datasheetModal'); alert('Datasheet Sent!');" style="padding: 24px;">
                <div class="form-group-custom" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px;">
                    <label style="font-size: 12px; font-weight: 500; color: #374151;">Your Email <span style="color: #6b7280;">*</span></label>
                    <input type="email" placeholder="example@gmail.com" required style="padding: 12px 16px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 14px; color: #111;">
                </div>
                <div class="form-group-custom" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="font-size: 12px; font-weight: 500; color: #374151;">Your Contact <span style="color: #6b7280;">(Optional)</span></label>
                    <input type="tel" placeholder="+91-0000000000" style="padding: 12px 16px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 14px; color: #111;">
                </div>
                <div class="brochure-submit-wrapper" style="display: flex; justify-content: flex-end;">
                    <button type="submit" class="btn btn-submit-brochure" style="background-color: #cbd5e1; color: #fff; border: none; padding: 10px 20px; border-radius: 6px; font-weight: 500; font-size: 14px; cursor: pointer;">Download Brochure</button>
                </div>
            </form>
        </div>
    </div>"""
    
    result = result.replace(old_modal, new_modal)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
        print("Success swapping elements")
else:
    print("Could not find section markers")
