# Elite Academy - School Website

A modern, responsive, and visually appealing school website built with pure HTML and CSS (no frameworks). This website showcases the school's information, facilities, and provides functionality for admissions and user authentication.

## Features

### 🎨 Design & UX
- **Professional Color Palette**: Deep blue (#1e3c72), vibrant cyan (#00d4ff), and accent orange (#ff9a00)
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern Animations**: Smooth transitions, hover effects, and scroll animations
- **Clean Typography**: Professional font hierarchy with excellent readability
- **Accessible Layout**: Proper semantic HTML and ARIA labels

### 📱 Pages & Sections

#### 1. **Home Page (home.html)**
   - **Hero Section**: Eye-catching introduction with call-to-action buttons
   - **About Section**: School history, mission, and key features
   - **Facilities Section**: Grid showcase of 6 major facilities with icons
   - **Highlights Section**: Key statistics (success rate, student count, etc.)
   - **Gallery Section**: Image gallery with hover overlays
   - **CTA Section**: Call-to-action for enrollment

#### 2. **Navigation Bar (base.html)**
   - Sticky navigation with smooth scrolling
   - Logo with icon
   - Links to: Home, About, Facilities, Gallery
   - Login and Sign Up buttons with distinct styling
   - Mobile-responsive hamburger menu
   - Active link indicators

#### 3. **Login Page (login_page.html)**
   - Clean form design with smooth animations
   - Email and password fields
   - "Remember me" checkbox
   - "Forgot password?" link
   - Link to sign up page
   - Responsive form layout

#### 4. **Sign Up Page (sign_up.html)**
   - Multi-field registration form
   - Fields: First name, last name, email, grade, password
   - Terms and conditions acceptance
   - Form validation support
   - Link to login page

#### 5. **Admission Form (admission_form.html)**
   - Comprehensive application form with sections:
     - Personal Information (name, DOB, gender, contact)
     - Academic Information (grade, current school, percentage)
     - Address Information (full address details)
     - Parent/Guardian Information
     - Additional Information (achievements, interests)
     - Document Upload (report card)
   - File upload with drag-and-drop styling
   - Submit and Reset buttons

#### 6. **Footer (base.html)**
   - Quick links section
   - Contact information with icons
   - Social media links (Facebook, Twitter, Instagram, LinkedIn)
   - Brand description
   - Copyright and legal links

### 🛠️ Technical Stack

- **HTML5**: Semantic markup structure
- **CSS3**: Advanced styling with:
  - CSS Grid and Flexbox layouts
  - CSS Variables for theming
  - Gradients and backdrop filters
  - Smooth transitions and animations
  - Media queries for responsiveness
- **JavaScript**: Vanilla JS for:
  - Mobile menu toggle
  - Smooth scrolling navigation
  - Intersection Observer for scroll animations
  - Active nav link highlighting

### 🎯 Key Design Elements

1. **Color Scheme**
   - Primary: #1e3c72 (Deep Blue)
   - Secondary: #2a5298 (Medium Blue)
   - Accent: #ff9a00 (Orange)
   - Light Accent: #00d4ff (Cyan)

2. **Typography**
   - Font Family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
   - Clean hierarchy from h1 to h6
   - Optimal line-height for readability

3. **Spacing**
   - Consistent padding and margins
   - Proper use of whitespace
   - Grid-based layout system

4. **Interactive Elements**
   - Buttons with hover effects and shadows
   - Links with underline animations
   - Cards with lift animations on hover
   - Form inputs with focus states

5. **Responsive Breakpoints**
   - Desktop: Full layout
   - Tablet (768px and below): Adjusted grid columns
   - Mobile (480px and below): Single column layout, stacked navigation

### 📁 File Structure

```
School_Admission_Website/
├── templates/
│   ├── base.html              # Main template with navbar & footer
│   ├── home.html              # Home page with all sections
│   ├── login_page.html        # User login form
│   ├── sign_up.html           # User registration form
│   └── admission_form.html    # School admission form
├── static/
│   ├── styles.css             # Main stylesheet (all styling)
│   ├── script.js              # JavaScript functionality
│   └── navbar.css             # (Original - deprecated)
├── manage.py                  # Django management script
├── db.sqlite3                 # Database file
└── School_Admission_Website/  # Django settings folder
```

### 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install django
   ```

2. **Run Django Development Server**
   ```bash
   python manage.py runserver
   ```

3. **Access the Website**
   - Home: `http://localhost:8000/`
   - Login: `http://localhost:8000/login`
   - Sign Up: `http://localhost:8000/signup`
   - Admission Form: `http://localhost:8000/admission`

### ✨ Features Implemented

✅ Modern navbar with responsive mobile menu
✅ Hero section with call-to-action buttons
✅ About section with feature highlights
✅ Facilities showcase with 6 different facilities
✅ Statistics section with key highlights
✅ Image gallery with hover effects
✅ Professional login page
✅ User registration/sign-up form
✅ Comprehensive admission form
✅ Complete footer with contact info and social links
✅ Fully responsive design (mobile, tablet, desktop)
✅ Smooth scrolling and animations
✅ Hover effects on interactive elements
✅ Professional color palette
✅ Clean, well-organized code
✅ Font Awesome icons integration
✅ CSS Grid and Flexbox layouts
✅ CSS variables for easy theming

### 📱 Responsive Design Features

- **Mobile Menu**: Hamburger menu for screens below 768px
- **Flexible Layouts**: Grid columns adjust based on screen size
- **Touch-Friendly**: Larger touch targets on mobile
- **Optimized Typography**: Font sizes adjust for readability
- **Image Placeholders**: Scalable icons for missing images

### 🎭 Animation & Effects

- **Fade-in animations** on scroll
- **Slide-in animations** on hero section
- **Hover scale effects** on cards
- **Smooth color transitions** on links
- **Lift effects** on buttons and cards
- **Border animations** on nav links
- **Float animations** in hero background

### 🔧 Customization

To customize colors, update the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #1e3c72;
    --secondary-color: #2a5298;
    --accent-color: #ff9a00;
    --light-accent: #00d4ff;
    /* ... more variables */
}
```

### 🎓 Best Practices

- Semantic HTML structure
- DRY (Don't Repeat Yourself) CSS with variables
- Mobile-first responsive design
- Accessibility considerations
- Performance optimization
- Clean code organization
- Proper form handling

### 📝 Notes

- Images are currently placeholder divs with icons from Font Awesome
- Replace image placeholders with actual images by updating the HTML
- Forms require backend Django views to process submissions
- All styling is in `styles.css` - no external CSS frameworks used
- JavaScript is vanilla - no jQuery or other libraries needed

### 🔐 Security Notes

- CSRF tokens included in forms (Django)
- Form validation can be implemented in views
- Ensure proper password handling in backend
- Validate file uploads on server-side

---

**Created**: 2024
**Version**: 1.0
**Status**: Production Ready
