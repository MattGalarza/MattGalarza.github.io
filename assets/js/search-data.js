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
          description: "Research in nonlinear dynamics, energy harvesting, scientific machine learning, and thermal transport.",
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
        },{id: "nav-cv",
          title: "cv",
          description: "Education, research, engineering experience, teaching, and technical skills.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-contributed-to-two-itherm-2025-papers-on-experimental-thermal-characterization-of-beol-materials-and-multiscale-thermal-analysis-of-3di-chip-stacks",
          title: 'Contributed to two ITherm 2025 papers on experimental thermal characterization of BEOL materials...',
          description: "",
          section: "News",},{id: "news-our-article-investigation-of-nonlinear-phenomena-in-electrically-coupled-mechanical-oscillators-with-applications-in-electrostatic-energy-harvesting-of-low-frequency-vibrations-was-published-in-the-journal-of-vibration-and-acoustics",
          title: 'Our article, “Investigation of Nonlinear Phenomena in Electrically Coupled Mechanical Oscillators With Applications...',
          description: "",
          section: "News",},{id: "news-completed-a-mechatronics-and-robotics-fellowship-at-ge-aerospace-research-developing-robotics-enabled-tools-for-in-situ-engine-inspection-and-dimensional-metrology",
          title: 'Completed a Mechatronics and Robotics Fellowship at GE Aerospace Research, developing robotics-enabled tools...',
          description: "",
          section: "News",},{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/MattGalarza", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6D%67%61%6C%61%72%7A%61.%72%70%69@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-inspire',
        title: 'Inspire HEP',
        section: 'Socials',
        handler: () => {
          window.open("https://inspirehep.net/authors/1010907", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/mgalarza1", "_blank");
        },
      },{
        id: 'social-researchgate',
        title: 'ResearchGate',
        section: 'Socials',
        handler: () => {
          window.open("https://www.researchgate.net/profile/Matthew-Galarza/", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=vc0aMmYAAAAJ", "_blank");
        },
      },{
        id: 'social-work',
        title: 'Work',
        section: 'Socials',
        handler: () => {
          window.open("https://www.rpi.edu/", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
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
