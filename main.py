import os
from dotenv import load_dotenv
from agents import financial_team
from data_processor import DataProcessor
from report_generator import ReportGenerator


load_dotenv()

def main():
    """Main function to run financial analysis"""
    
    print("🚀 Starting Financial Multi-Agent Analysis System\n")
    
    # Initialize components
    processor = DataProcessor()
    report_gen = ReportGenerator()
    
    # Example: Process sample data files
    print("📂 Processing data files...")
    
   
    
    # You can process real files like this:
    data = processor.process_csv("/Users/hritwizyash/Desktop/financial-multi-agent/data/financial_data.csv")

    
    print("🤖 Running multi-agent analysis...\n")
    
    #Create analysis query
    query = f"""
    Analyze the following financial information:
    
    {data}
    Also analyze Apple (AAPL) stock:
    1. Get current stock price and fundamentals
    2. Assess financial risks
    3. Provide strategic recommendations
    
    Summarize findings in a structured report format.
    """
    
    # Run multi-agent team
    print("=" * 60)
    response = financial_team.print_response(query, stream=True)
    print("\n" + "=" * 60)
    
    # Generate PDF report
    print("\n📄 Generating PDF report...")
    report_gen.generate_pdf(
        content=str(response),
        output_file="output/financial_report.pdf"
    )
    
    print("\n Analysis complete!")
    print("📊 Check 'output/financial_report.pdf' for the full report")

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    main()
