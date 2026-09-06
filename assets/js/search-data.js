// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "Peer-reviewed journal articles and conference proceedings.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-research",
          title: "research",
          description: "A portfolio of active and past research projects in nonlinear dynamics, energy harvesting, scientific machine learning, and thermal transport.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-software",
          title: "software",
          description: "Open-source models and computational tools supporting my research.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "Education, research, engineering experience, teaching, and technical skills.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "post-ai-may-not-become-human-the-world-may-become-less-human",
      
        title: "AI May Not Become Human. The World May Become Less Human.",
      
      description: "The greatest risk of artificial intelligence may be that we rebuild society around the things machines can understand.",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2026/ai-may-not-become-human/";
        
      },
    },{id: "news-contributed-to-two-itherm-2025-papers-on-experimental-thermal-characterization-of-beol-materials-and-multiscale-thermal-analysis-of-3di-chip-stacks",
          title: 'Contributed to two ITherm 2025 papers on experimental thermal characterization of BEOL materials...',
          description: "",
          section: "News",},{id: "news-completed-my-time-as-a-mechatronics-and-robotics-fellow-at-ge-aerospace-research-developing-robotics-enabled-tools-for-in-situ-engine-inspection-and-dimensional-metrology",
          title: 'Completed my time as a Mechatronics and Robotics Fellow at GE Aerospace Research,...',
          description: "",
          section: "News",},{id: "news-successfully-passed-my-candidacy-examination",
          title: 'Successfully passed my Candidacy examination!',
          description: "",
          section: "News",},{id: "news-successfully-developed-a-process-to-deposit-sub-100nm-testing-structures-for-thin-film-metrology-work-sponsored-by-ibm-with-help-to-my-friend-and-colleague-jonas-sem-measurement-of-the-deposited-heater-structure-thin-film-fabrication-in-the-rpi-cleanroom",
          title: 'Successfully developed a process to deposit sub-100nm testing structures for thin-film metrology work...',
          description: "",
          section: "News",},{id: "news-i-will-be-presenting-my-research-at-the-37th-annual-electronics-packaging-symposium-held-september-9-10-2026-at-binghamton-university-s-innovative-technologies-complex",
          title: 'I will be presenting my research at the 37th Annual Electronics Packaging Symposium,...',
          description: "",
          section: "News",},{id: "news-i-will-be-presenting-my-research-at-the-2026-albany-nanotechnology-symposium-ans-held-october-22-23-at-the-university-of-albany",
          title: 'I will be presenting my research at the 2026 Albany Nanotechnology Symposium (ANS),...',
          description: "",
          section: "News",},{id: "projects-coupled-nonlinear-dynamics",
          title: 'coupled nonlinear dynamics',
          description: "Developing energy-based descriptions of modal interaction, stability, and transport in coupled oscillator networks.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_nonlinear_dynamics/";
            },},{id: "projects-scientific-machine-learning-and-system-identification",
          title: 'scientific machine learning and system identification',
          description: "Combining first-principles models with interpretable data-driven methods for uncertain and unresolved dynamics.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_scientific_machine_learning/";
            },},{id: "projects-electrostatic-mems-energy-harvesting",
          title: 'electrostatic MEMS energy harvesting',
          description: "Designing broadband, low-frequency electromechanical systems that convert ambient vibration into electrical energy.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_mems_energy_harvesting/";
            },},{id: "projects-semiconductor-thin-film-thermal-transport",
          title: 'semiconductor thin-film thermal transport',
          description: "Measuring anisotropic thermal properties in BEOL and multilayer films for next-generation semiconductor packaging.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_thermal_transport/";
            },},{id: "projects-engineering-translation-and-experimental-systems",
          title: 'engineering translation and experimental systems',
          description: "Turning analytical concepts into testable hardware, automated workflows, and inspection tools for real engineering environments.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_engineering_translation/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6D%67%61%6C%61%72%7A%61.%72%70%69@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/mgalarza1", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=vc0aMmYAAAAJ", "_blank");
        },
      },{
        id: 'social-researchgate',
        title: 'ResearchGate',
        section: 'Socials',
        handler: () => {
          window.open("https://www.researchgate.net/profile/Matthew-Galarza/", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/MattGalarza", "_blank");
        },
      },{
        id: 'social-work',
        title: 'Work',
        section: 'Socials',
        handler: () => {
          window.open("https://www.rpi.edu/", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
