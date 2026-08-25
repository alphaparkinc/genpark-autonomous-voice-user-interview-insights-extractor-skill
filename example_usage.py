from client import AutonomousVoiceUserInterviewInsightsExtractorClient

def main():
    client = AutonomousVoiceUserInterviewInsightsExtractorClient()
    res = client.conduct_autonomous_user_interview_analysis('STUDY_ENTERPRISE_API_ADOPTION', 50)
    print('Study: ' + res['study_id'] + ' (' + str(res['interviews_conducted_by_voice_agent']) + ' voice interviews)')
    print('Top Needs: ' + ', '.join(res['top_unmet_user_needs']))
    print('NPS Correlation: ' + str(res['sentiment_nps_correlation_score']) + ' | Highlight Reel: ' + str(res['executive_video_clip_reel_compiled']))

if __name__ == '__main__':
    main()
