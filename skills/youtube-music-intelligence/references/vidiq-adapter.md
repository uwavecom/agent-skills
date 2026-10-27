# vidIQ adapter: discovery and spend controls

Use the connector's actual, currently documented tools. The tool names below are capabilities observed in the vidIQ integration in October 2026, not a guarantee of permanent availability.

| Purpose | Tool | Typical usage |
|---|---|---|
| Find channels, videos | `vidiq_youtube_search` | Specify a music topic, language and result type |
| Channel growth | `vidiq_channel_stats` | One competitor and an observation window |
| Channel uploads | `vidiq_channel_videos` | Recent or popular, long-form or Shorts |
| Breakouts | `vidiq_outliers` | Language, music theme, subscriber range and time window |
| Current momentum | `vidiq_trending_videos` | Subject in title query, VPH ordering |
| Keyword demand | `vidiq_keyword_research` | Relevant local-language phrases |
| Similar thumbnail references | `vidiq_similar_thumbnails` | Existing video ID or visual description |
| Batch video snapshot | `vidiq_get_videos_by_ids` | Prefer one call for up to 50 known videos |
| Batch channel snapshot | `vidiq_get_channels_by_ids` | Prefer one call for up to 50 known channels |
| Owned channels | `vidiq_user_channels` | Identify authorized channel before private analytics |

Many research actions have been priced at **5 vidIQ credits per call**, but prices and entitlements must be read from the live tool description before execution. Some identification calls may be free. Do not promise any fixed price or run multiple credits without explicit approval.

Example bounded study (only after approval):
1. Search for music channels/videos: one call.
2. Find breakout examples: one call.
3. Fetch known selected video IDs in one batch: one call.

If each action is currently 5 credits, estimated total = 15. The estimate is conditional, not a committed spend.

**Language constraint:** some vidIQ tools support Ukrainian-language long-form outlier research but not Ukrainian-language Shorts in the same method. Never silently switch Shorts searches to English; use an alternative search and mark the coverage limitation.

**Interpretation:**
- VPH is a recent velocity snapshot, not a historical audience trend.
- Outlier measures performance relative to a channel baseline; its exact algorithm may be proprietary.
- Tags and SEO optimization scores are weak proxies for viewer demand.
- A public competitor analysis lacks watch time, CTR, retention and confirmed acquisition sources.
- Source timestamps are required to compare successive snapshots.

## Fallback

If the vidIQ connector is unavailable, use user-provided CSV exports/screenshots or verifiable public YouTube data, recording fields that are not observable. Never scrape private or authenticated pages without authorization, and never fabricate outlier/VPH values from total views.
