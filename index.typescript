import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { motion } from 'framer-motion';

// Sample data tuned for an Analyst role
const profile = {
  name: 'Kishlay Kumar',
  title: 'Data & Web Scraping Analyst',
  location: 'India',
  summary:
    'Analytical-minded professional with 1+ years experience in software testing, web scraping and data analysis. I transform noisy data into reliable insights and automate repetitive workflows to accelerate decisions.',
  email: 'kishlay@example.com',
  phone: '+91 98765 43210',
  linkedin: 'https://www.linkedin.com/in/-kishlaykumar-',
};

const skills = [
  { name: 'Python', level: 90 },
  { name: 'Web Scraping (BeautifulSoup, Requests)', level: 88 },
  { name: 'Selenium / Playwright', level: 80 },
  { name: 'SQL & Databases', level: 85 },
  { name: 'Pandas / NumPy', level: 87 },
  { name: 'Testing & QA', level: 82 },
  { name: 'Data Visualization', level: 78 },
  { name: 'React (Frontend)', level: 70 },
];

const experience = [
  {
    role: 'Freelance Project Consultant',
    company: 'Self-employed',
    period: 'Sep 2023 - Present',
    bullets: [
      'Built automated scraping pipelines to collect financial and product data from 50+ sources.',
      'Validated and normalized incoming feeds; reduced data-cleaning time by 60%.',
      'Delivered dashboards and CSV deliverables to clients on schedule.' ,
    ],
  },
  {
    role: 'Programmer Analyst Intern',
    company: 'Cognizant Technology Solutions',
    period: 'Mar 2023 - Jul 2023',
    bullets: [
      'Contributed to backend testing and automation frameworks.',
      'Performed data validation and created end-to-end test cases.',
    ],
  },
];

const projects = [
  {
    title: 'E-Commerce Price Scraper & Analyzer',
    desc: 'End-to-end scraper pipeline that collects, deduplicates and analyzes pricing across multiple retailers for competitor benchmarking.',
    tech: ['Python', 'Requests', 'SQLite', 'Pandas', 'Matplotlib'],
    link: '#',
  },
  {
    title: 'Instagram Engagement Monitor (Prototype)',
    desc: 'A Selenium-based script to collect likes/comments metadata per-post and summarize engagement trends.',
    tech: ['Selenium', 'Python', 'Pandas'],
    link: '#',
  },
  {
    title: 'Automated Test Runner & Reporter',
    desc: 'A test harness that runs suites, captures logs and generates HTML reports for QA teams.',
    tech: ['PyTest', 'Python', 'Jenkins'],
    link: '#',
  },
];

// Small utility components
const Container = ({ children }) => (
  <div className="max-w-5xl mx-auto px-6 sm:px-8 py-10">{children}</div>
);

const navItems = [
  { to: '/', label: 'Home' },
  { to: '/about', label: 'About' },
  { to: '/skills', label: 'Skills' },
  { to: '/experience', label: 'Experience' },
  { to: '/projects', label: 'Projects' },
  { to: '/contact', label: 'Contact' },
];

function Navbar() {
  return (
    <nav className="w-full bg-gradient-to-r from-slate-800 via-slate-900 to-black text-white sticky top-0 z-40 shadow-lg">
      <Container>
        <div className="flex items-center justify-between py-4">
          <Link to="/" className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-gradient-to-r from-indigo-500 to-pink-500 flex items-center justify-center font-bold">KK</div>
            <div>
              <div className="font-semibold">{profile.name}</div>
              <div className="text-xs opacity-70">{profile.title}</div>
            </div>
          </Link>

          <div className="hidden md:flex gap-6 items-center">
            {navItems.map((n) => (
              <Link key={n.to} to={n.to} className="text-sm hover:opacity-90 transition-opacity">
                {n.label}
              </Link>
            ))}
            <a
              href={profile.linkedin}
              target="_blank"
              rel="noreferrer"
              className="text-sm px-3 py-1 bg-indigo-600 rounded-md shadow-sm hover:brightness-110"
            >
              LinkedIn
            </a>
          </div>

          <div className="md:hidden">
            <MobileMenu />
          </div>
        </div>
      </Container>
    </nav>
  );
}

function MobileMenu() {
  const [open, setOpen] = React.useState(false);
  return (
    <div className="relative">
      <button
        onClick={() => setOpen((s) => !s)}
        className="p-2 rounded-md bg-white/10 hover:bg-white/20"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
          <path d="M4 6h16M4 12h16M4 18h16" stroke="white" strokeWidth="1.6" strokeLinecap="round" />
        </svg>
      </button>

      {open && (
        <motion.div
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className="absolute right-0 mt-2 w-48 bg-slate-900 p-3 rounded-md shadow-lg"
        >
          <div className="flex flex-col gap-2">
            {navItems.map((n) => (
              <Link key={n.to} to={n.to} onClick={() => setOpen(false)} className="text-white">
                {n.label}
              </Link>
            ))}
            <a href={profile.linkedin} target="_blank" rel="noreferrer" className="text-white">
              LinkedIn
            </a>
          </div>
        </motion.div>
      )}
    </div>
  );
}

function Home() {
  return (
    <Container>
      <motion.section
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-8 items-center"
      >
        <div className="md:col-span-2">
          <motion.h1
            initial={{ x: -20, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ delay: 0.1 }}
            className="text-4xl sm:text-5xl font-extrabold leading-tight"
          >
            Hi, I'm {profile.name} — a <span className="text-indigo-500">Data & Web Scraping Analyst</span>.
          </motion.h1>

          <motion.p className="mt-5 text-lg text-slate-300" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.2 }}>
            {profile.summary}
          </motion.p>

          <div className="mt-6 flex gap-3">
            <Link to="/projects" className="inline-block px-5 py-3 bg-indigo-600 rounded-md font-medium shadow hover:scale-105 transform transition">
              View Projects
            </Link>
            <Link to="/contact" className="inline-block px-5 py-3 border rounded-md font-medium hover:opacity-90">
              Get in touch
            </Link>
          </div>

          <motion.div className="mt-8 grid grid-cols-3 gap-3 text-sm text-slate-300" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.35 }}>
            <StatCard label="Years Experience" value="1+" />
            <StatCard label="Tools" value="Python, SQL" />
            <StatCard label="Open-source" value="Contribs" />
          </motion.div>
        </div>

        <motion.div
          className="bg-gradient-to-tr from-slate-800 to-slate-900 p-6 rounded-2xl border border-white/5"
          initial={{ scale: 0.98, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          <div className="w-full flex flex-col items-center gap-4">
            <div className="w-32 h-32 rounded-full bg-gradient-to-r from-indigo-500 to-pink-500 flex items-center justify-center text-white text-2xl font-bold">KK</div>
            <div className="text-center">
              <div className="font-semibold text-lg">{profile.name}</div>
              <div className="text-sm opacity-70">{profile.title}</div>
            </div>

            <div className="w-full mt-3">
              <ContactMini />
            </div>
          </div>
        </motion.div>
      </motion.section>

      <motion.section className="mt-14" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5 }}>
        <h3 className="text-xl font-semibold">Highlighted Skills</h3>
        <div className="mt-4 grid grid-cols-2 md:grid-cols-4 gap-4">
          {skills.slice(0, 4).map((s) => (
            <div key={s.name} className="p-4 bg-white/3 rounded-md">
              <div className="flex justify-between items-center">
                <div className="font-medium">{s.name}</div>
                <div className="text-sm opacity-70">{s.level}%</div>
              </div>
              <div className="h-2 bg-white/10 rounded-full mt-3 overflow-hidden">
                <div className="h-full bg-gradient-to-r from-indigo-500 to-pink-500" style={{ width: `${s.level}%` }} />
              </div>
            </div>
          ))}
        </div>
      </motion.section>
    </Container>
  );
}

function StatCard({ label, value }) {
  return (
    <div className="p-3 bg-white/3 rounded-md">
      <div className="text-2xl font-bold">{value}</div>
      <div className="text-xs opacity-70 mt-1">{label}</div>
    </div>
  );
}

function ContactMini() {
  return (
    <div className="text-sm text-slate-200">
      <div className="flex items-center gap-3">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" className="opacity-80"><path d="M3 7v10l4-3 4 3 4-3 4 3V7" stroke="white" strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round" /></svg>
        <div>{profile.location}</div>
      </div>
      <div className="mt-2">
        <div className="font-medium">{profile.email}</div>
        <div className="text-xs opacity-70">{profile.phone}</div>
      </div>
    </div>
  );
}

function About() {
  return (
    <Container>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
        <h2 className="text-3xl font-bold">About Me</h2>
        <p className="mt-4 text-slate-300 leading-relaxed">
          {profile.summary} I focus on building robust data pipelines, end-to-end scraping solutions and clear reproducible analysis. I enjoy turning ambiguous requirements into testable workflows and delivering readable reports and visualizations that stakeholders trust.
        </p>

        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white/3 p-5 rounded-lg">
            <h4 className="font-semibold">Core Strengths</h4>
            <ul className="mt-3 list-disc list-inside text-slate-200">
              <li>Data collection & cleansing</li>
              <li>Automated testing and validation</li>
              <li>ETL & Scheduling</li>
              <li>Stakeholder-facing reports</li>
            </ul>
          </div>

          <div className="bg-white/3 p-5 rounded-lg">
            <h4 className="font-semibold">Tools & Platforms</h4>
            <div className="mt-3 flex flex-wrap gap-2">
              {skills.map((s) => (
                <span key={s.name} className="px-3 py-1 bg-white/6 rounded-full text-sm">{s.name}</span>
              ))}
            </div>
          </div>
        </div>
      </motion.div>
    </Container>
  );
}

function Skills() {
  return (
    <Container>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
        <h2 className="text-3xl font-bold">Skills</h2>
        <p className="mt-3 text-slate-300">Technical skills, libraries and methodologies I use every day.</p>

        <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white/3 p-5 rounded-lg">
            <h4 className="font-semibold">Technical</h4>
            <div className="mt-4 space-y-3">
              {skills.map((s) => (
                <SkillBar key={s.name} name={s.name} level={s.level} />
              ))}
            </div>
          </div>

          <div className="bg-white/3 p-5 rounded-lg">
            <h4 className="font-semibold">Methodologies</h4>
            <ul className="mt-4 list-disc list-inside text-slate-200">
              <li>Test-Driven Development & Automated Tests</li>
              <li>Version Control & Code Reviews</li>
              <li>Data Validation & Schema Checks</li>
              <li>Agile / Scrum Collaboration</li>
            </ul>
          </div>
        </div>
      </motion.div>
    </Container>
  );
}

function SkillBar({ name, level }) {
  return (
    <div>
      <div className="flex justify-between text-sm">
        <div>{name}</div>
        <div className="opacity-70">{level}%</div>
      </div>
      <div className="h-2 bg-white/10 rounded-full mt-2 overflow-hidden">
        <motion.div initial={{ width: 0 }} animate={{ width: `${level}%` }} transition={{ duration: 0.8 }} className="h-full bg-gradient-to-r from-indigo-500 to-pink-500" />
      </div>
    </div>
  );
}

function Experience() {
  return (
    <Container>
      <h2 className="text-3xl font-bold">Work Experience</h2>
      <div className="mt-6 space-y-6">
        {experience.map((e) => (
          <motion.div key={e.role} initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }} className="bg-white/3 p-5 rounded-lg">
            <div className="flex justify-between items-center">
              <div>
                <div className="font-semibold text-lg">{e.role}</div>
                <div className="text-sm opacity-80">{e.company}</div>
              </div>
              <div className="text-sm opacity-70">{e.period}</div>
            </div>

            <ul className="mt-3 list-disc list-inside text-slate-200">
              {e.bullets.map((b, i) => (
                <li key={i}>{b}</li>
              ))}
            </ul>
          </motion.div>
        ))}
      </div>
    </Container>
  );
}

function Projects() {
  return (
    <Container>
      <h2 className="text-3xl font-bold">Projects</h2>
      <p className="mt-3 text-slate-300">Selected projects that showcase analysis, automation and product-focused thinking.</p>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        {projects.map((p) => (
          <motion.div key={p.title} whileHover={{ y: -6 }} className="bg-white/3 p-5 rounded-lg border border-white/5">
            <div className="flex justify-between items-start gap-3">
              <div>
                <div className="font-semibold text-lg">{p.title}</div>
                <div className="text-sm opacity-80 mt-1">{p.desc}</div>
              </div>
              <div className="text-xs opacity-70">{p.tech.join(' • ')}</div>
            </div>

            <div className="mt-4 flex gap-2">
              <a href={p.link} className="text-sm px-3 py-2 border rounded-md">View</a>
              <button className="text-sm px-3 py-2 bg-indigo-600 rounded-md">Demo</button>
            </div>
          </motion.div>
        ))}
      </div>
    </Container>
  );
}

function Contact() {
  return (
    <Container>
      <h2 className="text-3xl font-bold">Contact</h2>
      <p className="mt-3 text-slate-300">I’m open to freelance and full-time opportunities — especially projects that need robust data pipelines and reliable automation.</p>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white/3 p-6 rounded-lg">
          <h4 className="font-semibold">Get in touch</h4>
          <div className="mt-4 text-sm text-slate-200">
            <div>Email: {profile.email}</div>
            <div className="mt-1">Phone: {profile.phone}</div>
            <div className="mt-1">Location: {profile.location}</div>
          </div>

          <form className="mt-6 space-y-3" onSubmit={(e) => e.preventDefault()}>
            <input type="text" placeholder="Your name" className="w-full p-3 rounded-md bg-white/5" />
            <input type="email" placeholder="Email" className="w-full p-3 rounded-md bg-white/5" />
            <textarea placeholder="Message" className="w-full p-3 rounded-md bg-white/5 h-28" />
            <button className="px-5 py-3 bg-indigo-600 rounded-md">Send message</button>
          </form>
        </div>

        <div className="bg-white/3 p-6 rounded-lg">
          <h4 className="font-semibold">Quick links</h4>
          <div className="mt-4 flex flex-col gap-2 text-sm">
            <a href={profile.linkedin} target="_blank" rel="noreferrer" className="underline">LinkedIn</a>
            <a href="#" className="underline">GitHub</a>
            <a href="#" className="underline">Resume (PDF)</a>
          </div>

          <div className="mt-6">
            <h5 className="font-medium">Follow</h5>
            <div className="flex gap-3 mt-3">
              <a href="#" className="px-3 py-2 bg-white/5 rounded-md">Twitter</a>
              <a href="#" className="px-3 py-2 bg-white/5 rounded-md">Medium</a>
            </div>
          </div>
        </div>
      </div>
    </Container>
  );
}

function Footer() {
  return (
    <footer className="mt-16 py-8 text-center text-sm text-slate-400">
      <Container>
        <div>© {new Date().getFullYear()} {profile.name}. Built with React + Tailwind + Framer Motion.</div>
      </Container>
    </footer>
  );
}

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-b from-slate-950 to-slate-900 text-white"> 
        <Navbar />

        <main className="pt-8 pb-16">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/skills" element={<Skills />} />
            <Route path="/experience" element={<Experience />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="*" element={<Home />} />
          </Routes>
        </main>

        <Footer />
      </div>
    </Router>
  );
}
