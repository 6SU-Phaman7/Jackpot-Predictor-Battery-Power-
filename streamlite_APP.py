import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Battery Sports Predictor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the "Battery" Branding
st.markdown("""
    <style>
    .main {
        background-color: #020617;
    }
    .stMetric {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #334155;
    }
    .prediction-card {
        background-color: #0f172a;
        padding: 20px;
        border-radius: 20px;
        border-left: 5px solid #eab308;
        margin-bottom: 20px;
        border-top: 1px solid #1e293b;
        border-right: 1px solid #1e293b;
        border-bottom: 1px solid #1e293b;
    }
    .live-card {
        background-color: #0f172a;
        padding: 20px;
        border-radius: 20px;
        border-left: 5px solid #ef4444;
        margin-bottom: 20px;
    }
    .battery-text {
        color: #eab308;
        font-weight: 900;
    }
    </style>
    """, unsafe_allow_html=True)

# App Header
col_header1, col_header2 = st.columns([2, 1])
with col_header1:
    st.markdown("# ⚡ BATTERY <span style='color:#eab308'>PRO</span>", unsafe_allow_html=True)
    st.caption("AI-Driven Sports Predictions & Live Momentum Tracking")

with col_header2:
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if st.button("🔄 Refresh Signals"):
        with st.spinner("Re-charging Battery Predictions..."):
            time.sleep(1)
            st.rerun()

# Top Stats Row
st.markdown("### 📊 Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Today's Accuracy", "84.2%", "+2.1%")
col2.metric("Monthly ROI", "+148%", "High")
col3.metric("Live Win Streak", "7 Games", "🔥")
col4.metric("Active Signals", "14", "Stable")

# Tabs for Air Slips vs Live Radar
tab1, tab2 = st.tabs(["📑 PREDICTIVE AIR SLIPS", "📡 LIVE RADAR"])

with tab1:
    st.markdown("#### 🚀 Early Bird Predictions")
    
    # Mock Prediction Data
    preds = [
        {"match": "Man City vs Real Madrid", "market": "Over 2.5 Goals", "odds": 2.45, "charge": 92, "league": "Champions League"},
        {"match": "Lakers vs Celtics", "market": "Lakers +4.5", "odds": 1.90, "charge": 78, "league": "NBA"},
        {"match": "Springboks vs All Blacks", "market": "SA to Win", "odds": 1.75, "charge": 85, "league": "Rugby Championship"}
    ]

    for p in preds:
        with st.container():
            st.markdown(f"""
            <div class="prediction-card">
                <small style="color:#94a3b8">{p['league']}</small>
                <h3 style="margin:0;">{p['match']}</h3>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-top:15px;">
                    <div>
                        <p style="margin:0; font-size:12px; color:#64748b;">AI SELECTION</p>
                        <p style="margin:0; font-weight:bold; color:#eab308;">{p['market']}</p>
                    </div>
                    <div style="text-align:right;">
                        <p style="margin:0; font-size:12px; color:#64748b;">BATTERY CHARGE</p>
                        <p style="margin:0; font-weight:bold; color:#22c55e;">{p['charge']}%</p>
                    </div>
                </div>
                <hr style="opacity:0.1; margin:15px 0;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:24px; font-weight:900;">{p['odds']}</span>
                    <button style="background-color:#eab308; border:none; padding:5px 15px; border-radius:8px; font-weight:bold;">LOCK SLIP</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### 🔴 Real-Time Momentum Tracking")
    
    # Live Game Simulation
    live_match = "Arsenal vs Liverpool"
    score = "1 - 1"
    minute = "64'"
    
    st.markdown(f"""
    <div class="live-card">
        <div style="display:flex; justify-content:space-between;">
            <span style="color:#ef4444; font-weight:bold;">● LIVE {minute}</span>
            <span style="font-family:monospace; font-weight:bold;">{score}</span>
        </div>
        <h2 style="text-align:center; margin:20px 0;">{live_match}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Momentum Progress Bar
    momentum = st.slider("AI Momentum Score", 0, 100, 88)
    st.progress(momentum / 100)
    st.caption(f"Arsenal is currently maintaining {momentum}% pressure in the final third.")
    
    st.info(f"💡 **AI Suggestion:** High probability of Arsenal Next Goal. Live Odds: **3.10**")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; opacity:0.6;">
    <p style="font-size:10px;">
        OHLELEKILE FINANCIAL PROVIDER PTY(LTD) <br>
        RESPONSIBLE GAMBLING: 0800 006 008 <br>
        NO PERSONS UNDER 18. PREDICTIONS ARE PROBABILISTIC.
    </p>
</div>
""", unsafe_allow_html=True)      time: "Tomorrow 03:00",
      confidence: 78,
      type: "Stable Power",
      odds: "1.90",
      market: "Lakers +4.5",
      league: "NBA",
      status: "Pre-Match Value"
    },
    {
      id: 3,
      match: "Springboks vs All Blacks",
      time: "Sat 17:00",
      confidence: 85,
      type: "High Voltage",
      odds: "1.75",
      market: "SA to Win",
      league: "Rugby Championship",
      status: "Early Bird"
    }
  ];

  const liveGames = [
    {
      id: 101,
      match: "Arsenal vs Liverpool",
      score: "1 - 1",
      minute: "64'",
      prediction: "Arsenal Next Goal",
      liveOdds: "3.10",
      momentum: 88
    }
  ];

  const getBatteryIcon = (level) => {
    if (level >= 90) return <BatteryFull className="text-green-500" />;
    if (level >= 70) return <BatteryMedium className="text-yellow-500" />;
    return <BatteryLow className="text-red-500" />;
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans pb-20">
      {/* Header */}
      <header className="p-6 bg-slate-900 border-b border-slate-800 sticky top-0 z-50">
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="bg-yellow-500 p-2 rounded-lg">
              <Zap className="text-slate-950 fill-current" size={24} />
            </div>
            <h1 className="text-2xl font-black tracking-tighter italic">BATTERY <span className="text-yellow-500">PRO</span></h1>
          </div>
          <div className="flex gap-4">
            <button className="p-2 bg-slate-800 rounded-full"><Search size={20}/></button>
            <button className="p-2 bg-slate-800 rounded-full relative">
              <Bell size={20}/>
              <span className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full border-2 border-slate-900"></span>
            </button>
          </div>
        </div>
      </header>

      {/* Hero Stats */}
      <section className="p-6">
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-gradient-to-br from-indigo-600 to-indigo-800 p-4 rounded-2xl shadow-xl">
            <p className="text-xs text-indigo-200 uppercase font-bold">Today's Accuracy</p>
            <h3 className="text-2xl font-bold">84.2%</h3>
            <div className="mt-2 h-1 w-full bg-indigo-900 rounded-full overflow-hidden">
              <div className="h-full bg-white w-[84%]"></div>
            </div>
          </div>
          <div className="bg-gradient-to-br from-emerald-600 to-emerald-800 p-4 rounded-2xl shadow-xl">
            <p className="text-xs text-emerald-200 uppercase font-bold">Live Wins</p>
            <h3 className="text-2xl font-bold">+12</h3>
            <p className="text-[10px] mt-1 text-emerald-100 italic">Across 5 Leagues</p>
          </div>
        </div>
      </section>

      {/* Navigation Tabs */}
      <div className="px-6 flex gap-6 border-b border-slate-800">
        <button 
          onClick={() => setActiveTab('predictions')}
          className={`pb-3 text-sm font-bold transition-colors ${activeTab === 'predictions' ? 'text-yellow-500 border-b-2 border-yellow-500' : 'text-slate-400'}`}
        >
          AIR SLIPS
        </button>
        <button 
          onClick={() => setActiveTab('live')}
          className={`pb-3 text-sm font-bold transition-colors ${activeTab === 'live' ? 'text-yellow-500 border-b-2 border-yellow-500' : 'text-slate-400'}`}
        >
          LIVE RADAR
        </button>
      </div>

      <main className="p-6">
        {activeTab === 'predictions' ? (
          <div className="space-y-4">
            <div className="flex justify-between items-center mb-2">
              <h2 className="font-bold flex items-center gap-2"><TrendingUp size={18} className="text-yellow-500"/> Predictive Power</h2>
              <span className="text-xs text-slate-500">Updated: Just Now</span>
            </div>
            
            {predictions.map(pred => (
              <div key={pred.id} className="bg-slate-900 rounded-2xl p-5 border border-slate-800 hover:border-yellow-500/50 transition-all cursor-pointer group">
                <div className="flex justify-between items-start mb-3">
                  <div>
                    <span className="text-[10px] bg-slate-800 px-2 py-1 rounded-md text-slate-400 font-mono mb-1 inline-block uppercase tracking-widest">{pred.league}</span>
                    <h4 className="font-bold text-lg">{pred.match}</h4>
                  </div>
                  <div className="text-right">
                    <div className="flex items-center gap-1 justify-end">
                      {getBatteryIcon(pred.confidence)}
                      <span className="font-bold text-sm">{pred.confidence}%</span>
                    </div>
                    <p className="text-[10px] text-slate-500 uppercase font-bold">{pred.type}</p>
                  </div>
                </div>

                <div className="flex items-center justify-between mt-4 bg-slate-950 p-3 rounded-xl">
                  <div>
                    <p className="text-[10px] text-slate-500 uppercase tracking-tighter font-bold">Recommended Slip</p>
                    <p className="text-yellow-500 font-bold">{pred.market}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-[10px] text-slate-500 uppercase font-bold">Odds</p>
                    <p className="text-xl font-black text-white">{pred.odds}</p>
                  </div>
                </div>
                
                <div className="mt-3 flex items-center justify-between">
                  <span className="text-xs text-emerald-400 flex items-center gap-1">
                    <Activity size={12}/> {pred.status}
                  </span>
                  <ChevronRight size={16} className="text-slate-600 group-hover:text-yellow-500" />
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="space-y-4">
            <h2 className="font-bold flex items-center gap-2"><Activity size={18} className="text-red-500"/> Live Prediction Updates</h2>
            {liveGames.map(game => (
              <div key={game.id} className="bg-slate-900 rounded-2xl p-5 border-l-4 border-red-500">
                <div className="flex justify-between items-center mb-4">
                  <div className="flex items-center gap-2">
                    <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
                    <span className="text-xs font-bold text-red-500">LIVE {game.minute}</span>
                  </div>
                  <span className="text-lg font-mono font-bold">{game.score}</span>
                </div>
                <h4 className="font-bold text-center mb-4">{game.match}</h4>
                <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-xs text-slate-500 uppercase font-bold">AI Momentum</span>
                    <span className="text-xs font-bold text-white">{game.momentum}% Pressure</span>
                  </div>
                  <div className="h-2 w-full bg-slate-800 rounded-full mb-4">
                    <div className="h-full bg-gradient-to-r from-yellow-500 to-orange-500" style={{width: `${game.momentum}%`}}></div>
                  </div>
                  <div className="flex justify-between items-end">
                    <div>
                      <p className="text-[10px] text-slate-500">LIVE PREDICTION</p>
                      <p className="font-bold text-yellow-500">{game.prediction}</p>
                    </div>
                    <button className="bg-yellow-500 text-slate-950 px-4 py-2 rounded-lg font-bold text-sm">
                      BET @ {game.liveOdds}
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      {/* Responsible Gambling Footer */}
      <footer className="p-6 text-center border-t border-slate-900 opacity-50">
        <div className="flex justify-center gap-2 mb-2">
          <ShieldAlert size={14} className="text-yellow-500" />
          <span className="text-[10px] font-bold uppercase tracking-widest">Winners know when to stop</span>
        </div>
        <p className="text-[8px] text-slate-400 max-w-xs mx-auto">
          Ohlelekile Financial Provider PTY(Ltd). No persons under 18. NRGP: 0800 006 008. Gambling involves risk.
        </p>
      </footer>

      {/* Bottom Nav */}
      <nav className="fixed bottom-0 left-0 right-0 bg-slate-900 border-t border-slate-800 flex justify-around items-center p-3">
        <button className="flex flex-col items-center gap-1 text-yellow-500">
          <Trophy size={20} />
          <span className="text-[10px] font-bold">Predict</span>
        </button>
        <button className="flex flex-col items-center gap-1 text-slate-500 hover:text-white">
          <Clock size={20} />
          <span className="text-[10px] font-bold">History</span>
        </button>
        <div className="bg-yellow-500 p-3 rounded-full -mt-8 border-4 border-slate-950 shadow-xl shadow-yellow-500/20">
          <Zap className="text-slate-950 fill-current" size={24} />
        </div>
        <button className="flex flex-col items-center gap-1 text-slate-500 hover:text-white">
          <Activity size={20} />
          <span className="text-[10px] font-bold">Live</span>
        </button>
        <button className="flex flex-col items-center gap-1 text-slate-500 hover:text-white">
          <BatteryMedium size={20} />
          <span className="text-[10px] font-bold">Account</span>
        </button>
      </nav>
    </div>
  );
};

export default App;
