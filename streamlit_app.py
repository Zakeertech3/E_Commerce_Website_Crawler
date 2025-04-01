import streamlit as st
import asyncio
from crawler.main import run_crawler, DOMAINS
import json
import time
from datetime import datetime

st.set_page_config(page_title="Product URL Crawler", layout="wide")
st.title("🛒 Product URL Crawler Dashboard")
st.write("Crawl e-commerce domains for product URLs with enhanced performance and live visualization.")

if st.button("🚀 Start Crawling"):
    start_time = time.time()
    progress_bar = st.progress(0)
    status_text = st.empty()
    fetched_urls_table = st.empty()  # Placeholder for live updates of fetched URLs
    live_log = st.empty()  # Placeholder for live log updates
    
    with st.spinner("Crawling in progress... Please wait."):
        try:
            async def run_and_visualize():
                crawler_output = {}
                total_domains = len(DOMAINS)
                completed_domains = 0
                
                # Use async for to iterate over the async generator
                async for domain, urls in run_crawler():
                    completed_domains += 1
                    crawler_output[domain] = urls
                    progress_bar.progress(completed_domains / total_domains)
                    status_text.write(f"Fetched {len(urls)} URLs from {domain}")
                    
                    # Update the live table with fetched URLs
                    fetched_urls_table.write(f"### Fetched URLs for {domain}")
                    fetched_urls_table.table({"URLs": urls})
                    
                    # Update the live log
                    live_log.write(f"**Log:** Completed {completed_domains}/{total_domains} domains.")
                
                return crawler_output
            
            crawler_output = asyncio.run(run_and_visualize())
            elapsed_time = time.time() - start_time
            
            st.success(f"✅ Crawling completed in {elapsed_time:.2f} seconds!")
            
            # Display results in tabs
            tab1, tab2 = st.tabs(["📋 Results", "📊 Statistics"])
            
            with tab1:
                st.subheader("Crawled Product URLs")
                st.json(crawler_output)
            
            with tab2:
                st.subheader("Crawling Statistics")
                col1, col2 = st.columns(2)
                for domain, urls in crawler_output.items():
                    with col1 if len(urls) % 2 == 0 else col2:
                        st.metric(label=f"Domain: {domain}", value=f"{len(urls)} URLs")
            
            # Download options
            st.download_button(
                "💾 Download Results (JSON)",
                data=json.dumps(crawler_output, indent=4),
                file_name="crawler_results.json",
                mime="application/json"
            )
        except Exception as e:
            st.error(f"❌ Error during crawling: {str(e)}")
