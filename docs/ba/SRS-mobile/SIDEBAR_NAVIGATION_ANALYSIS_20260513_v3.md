# Assumptions & Best Practices — Sidebar Navigation (Cổng đầu tư Quốc gia trên Mobile)

**Tiêu đề:** Phân tích & Đề xuất cấu trúc Sidebar Mobile App  
**Ngày tạo:** 13/05/2026  
**Tác giả:** QC Agent  
**Phiên bản:** v3  
**Nguồn dữ liệu:** [MBFS - Cổng đầu tư QG] BA internal file .xlsx — Sheet "WBS (Mobile)"

---

## 1. Quyết định đã thống nhất (Q&A 13/05/2026)

| # | Hạng mục | Quyết định |
|---|----------|-----------|
| 1 | Scope hiển thị | In-scope + Out-of-scope (bỏ Cancel) |
| 2 | KCN/KKT (16 nhóm) | Gom thành 1 mục + bộ lọc bên trong trang |
| 3 | Danh mục "Quản lý Xúc tiến ĐT" | Giữ 1 nhóm duy nhất (đúng như Excel) |
| 4 | UC55-86 "Khai thác TT đã công bố" | Gom thành 1 mục "Thông tin đã công bố" |
| 5 | AI Chatbot | 1 mục trong sidebar (KHÔNG phải FAB) |
| 6 | Trang chủ | Có mục riêng đầu sidebar |
| 7 | Dashboard theo tài khoản | Gom vào Trang chủ (không mục riêng) |
| 8 | Nhắc hạn | Gom vào Thông báo (UC258-259) |
| 9 | Nhóm chưa rõ scope | Đưa vào sidebar (Phiên tư vấn, An toàn, Gợi ý, Thu thập nhu cầu) |
| 10 | Cấu trúc sidebar | Flat với section header (như wireframe hiện tại) |
| 11 | Thứ tự các section | Theo wireframe hiện tại |

---

## 2. Proposed Tree View — Sidebar (v3)

```
┌─────────────────────────────────────────────────┐
│  [Avatar] Nguyễn Văn A                          │
│  nguyenvana@example.com                         │
│  Xem hồ sơ                                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  Trang chủ (bao gồm Dashboard)                 │
│                                                 │
│  ── GIỚI THIỆU ──────────────────────────────  │
│  Giới thiệu                                    │
│  Lĩnh vực đầu tư                               │
│  Khu vực đầu tư                                │
│  Liên hệ                                       │
│                                                 │
│  ── DỊCH VỤ ─────────────────────────────────  │
│  Thủ tục hành chính                            │
│  Quản lý hồ sơ                                 │
│  Quản lý đặt lịch                              │
│  Phản ánh kiến nghị                            │
│  Báo cáo đầu tư                                │
│                                                 │
│  ── KHU CÔNG NGHIỆP / KKT ──────────────────  │
│  Tra cứu KCN / KKT                            │
│     └─ [Bộ lọc bên trong trang:]              │
│        • Khu công nghiệp                       │
│        • KCN sinh thái                         │
│        • KCN công nghệ cao                     │
│        • Khu kinh tế                           │
│        • Khu kinh tế ven biển                  │
│        • Khu kinh tế cửa khẩu                 │
│        • Khu kinh tế chuyên biệt              │
│        • Khu phi thuế quan                     │
│        • Khu thương mại tự do                  │
│        • Mô hình khu khác                      │
│  Dự án đầu tư KCN/KKT                         │
│  Thông tin quỹ đất                             │
│                                                 │
│  ── TIN TỨC & TRA CỨU ──────────────────────  │
│  Tin tức                                       │
│  Văn bản pháp luật                             │
│  FAQ                                           │
│  Hướng dẫn sử dụng                            │
│                                                 │
│  ── QUẢN LÝ XÚC TIẾN ĐẦU TƯ ───────────────  │
│  Quản lý đặt lịch nộp thủ tục                 │
│  Quản lý hồ sơ                                 │
│  Tra cứu kho dữ liệu điện tử                  │
│  Tra cứu phản ánh kiến nghị                   │
│  Tra cứu báo cáo NĐT đã nộp                   │
│  Thông tin đã công bố                          │
│  Khai thác thông tin xúc tiến đầu tư          │
│                                                 │
│  ── AI CHATBOT & CÁ NHÂN HOÁ ───────────────  │
│  AI Chatbot                                    │
│  Quản lý phiên tư vấn & lịch sử              │
│  An toàn, giới hạn tư vấn & kết nối hỗ trợ   │
│  Gợi ý và so sánh phương án đầu tư           │
│  Thu thập nhu cầu & cá nhân hoá tư vấn       │
│                                                 │
│  ── QUẢN LÝ CHUNG ──────────────────────────  │
│  Quản lý tài khoản nhà đầu tư                 │
│  Thông báo hệ thống (bao gồm Nhắc hạn)       │
│  Bản đồ số                                    │
│                                                 │
├─────────────────────────────────────────────────┤
│  Cấu hình tài khoản                           │
│  Đăng xuất                                     │
└─────────────────────────────────────────────────┘
```

---

## 3. Mapping Sidebar → Danh mục & Nhóm chức năng (Excel WBS)

### Danh mục: TRANG CHỦ

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| Trang chủ (bao gồm Dashboard) | Chứa các đường dẫn nhanh... | UC1 | Out-of-scope |
| *(Dashboard gom vào Trang chủ)* | Dashboard theo tài khoản trên mobile | UC244-248 | In scope |

### Danh mục: KHU CÔNG NGHIỆP / KKT

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| Tra cứu KCN/KKT (1 mục + bộ lọc) | Khai thác thông tin khu công nghiệp | UC2-6 | In scope |
| *(bộ lọc)* | Khai thác thông tin KCN sinh thái | UC17-21 | In scope |
| *(bộ lọc)* | Khai thác thông tin khu thương mại tự do | UC27-31 | In scope |
| *(bộ lọc)* | Khai thác thông tin khu kinh tế | UC7-11 | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin mô hình khu khác | UC12-16 | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin khu phi thuế quan | UC22-26 | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin KCN công nghệ cao | — | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin KKT ven biển | — | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin KKT cửa khẩu | — | Out-of-scope |
| *(bộ lọc)* | Khai thác thông tin KKT chuyên biệt | — | Out-of-scope |
| Dự án đầu tư KCN/KKT | Khai thác thông tin dự án đầu tư KCN/KKT | UC32-39 | In scope |
| Thông tin quỹ đất | Khai thác thông tin kiểm tra KCN, KTT (phần quỹ đất) | UC40 | Out-of-scope |

### Danh mục: QUẢN LÝ XÚC TIẾN ĐẦU TƯ TRÊN MOBILE

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| Quản lý đặt lịch nộp thủ tục | Quản lý đặt lịch nộp thủ tục về đầu tư | UC42-44 | In scope |
| Quản lý hồ sơ | Quản lý hồ sơ trên mobile | UC45-51 | In scope |
| Tra cứu kho dữ liệu điện tử | Tra cứu kho dữ liệu điện tử trên mobile | UC52 | In scope |
| Tra cứu phản ánh kiến nghị | Tra cứu phản ánh kiến nghị trên mobile | UC53, 63-65 | In scope |
| Tra cứu báo cáo NĐT đã nộp | Tra cứu báo cáo nhà đầu tư đã nộp | UC54 | In scope |
| Thông tin đã công bố | Khai thác thông tin đã công bố trên mobile | UC55-86 | In scope |
| Khai thác TT xúc tiến đầu tư | Khai thác thông tin xúc tiến đầu tư | UC87-95 | Hỗn hợp |

### Danh mục: AI CHATBOT & CÁ NHÂN HOÁ HỖ TRỢ NHÀ ĐẦU TƯ

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| AI Chatbot | (Gom 16 knowledge domain) | UC60-61, UC96-228 | Hỗn hợp |
| *(knowledge domains bên trong):* | Quy định chung | UC96-105 | Out-of-scope |
| | Ngành nghề và tiếp cận thị trường | UC106-117 | Out-of-scope |
| | Ưu đãi và hỗ trợ đầu tư | UC118-129 | Out-of-scope |
| | Hồ sơ và thủ tục đầu tư | UC130-144 | Out-of-scope |
| | Triển khai và chấp thuận dự án | UC145-156 | Out-of-scope |
| | Nghĩa vụ tài chính & ký quỹ | UC157-164 | Out-of-scope |
| | Triển khai và vận hành dự án | UC165-172 | Out-of-scope |
| | Điều chỉnh dự án | UC173-182 | Out-of-scope |
| | Chuyển nhượng và tái cấu trúc | UC183-190 | Out-of-scope |
| | Chấm dứt dự án | UC191-196 | Out-of-scope |
| | Quản lý nhà nước và xúc tiến | UC197-202 | Out-of-scope |
| | Báo cáo và giám sát | UC203-207 | Out-of-scope |
| | Chuyển tiếp và trường hợp đặc biệt | UC208-212 | Out-of-scope |
| | Đầu tư ra nước ngoài | UC213-222 | Out-of-scope |
| | Đa ngôn ngữ | UC223-227 | Out-of-scope |
| | Đánh giá câu trả lời | UC228 | Out-of-scope |
| Nhắc hạn *(gom vào Thông báo)* | Nhắc hạn trên mobile | UC229-243 | In scope |
| *(Dashboard gom vào Trang chủ)* | Dashboard theo tài khoản trên mobile | UC244-248 | In scope |
| Quản lý phiên tư vấn & lịch sử | Quản lý phiên tư vấn, lịch sử và tài liệu đầu ra | — | Chưa rõ scope |
| An toàn, giới hạn tư vấn & kết nối hỗ trợ | An toàn, giới hạn tư vấn và kết nối hỗ trợ | — | Chưa rõ scope |
| Gợi ý và so sánh phương án đầu tư | Gợi ý và so sánh phương án đầu tư | — | Chưa rõ scope |
| Thu thập nhu cầu & cá nhân hoá | Thu thập nhu cầu và cá nhân hoá tư vấn cho NĐT | — | Chưa rõ scope |

### Danh mục: QUẢN LÝ CHUNG TRÊN MOBILE

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| Quản lý tài khoản nhà đầu tư | Quản lý tài khoản nhà đầu tư trên mobile | UC249-255 | In scope |
| Thông báo hệ thống (bao gồm Nhắc hạn) | Quản lý thông tin chung trên mobile | UC258-259 | In scope |
| Đăng nhập | *(thuộc Quản lý thông tin chung)* | UC256 | In scope |
| Đăng xuất | *(thuộc Quản lý thông tin chung)* | UC257 | In scope |
| Cấu hình tài khoản | *(thuộc Quản lý tài khoản)* | UC254, UC260 | In scope |

### Danh mục: TÍCH HỢP

| Menu Item (Sidebar) | Nhóm chức năng (Excel) | UC IDs | Scope |
|---|---|---|---|
| Bản đồ số | Bản đồ số trên mobile | — | Chưa rõ scope |

---

## 4. Nhóm chức năng KHÔNG hiển thị trên Sidebar (Cancel)

> Các nhóm sau bị Cancel trong WBS, không cần thể hiện trên sidebar:

| Nhóm chức năng | Lý do Cancel |
|---|---|
| Khai thác thông tin khu chế xuất | Chưa phát triển |
| Khai thác thông tin KCN hỗ trợ | Chưa phát triển |
| Khai thác thông tin KCN chuyên ngành | Chưa phát triển |
| Tra cứu tổng hợp thông tin KCN/KKT | Chưa phát triển |
| Khai thác thông tin kiểm tra KCN, KTT (trừ UC40) | Chưa phát triển |

---

## 5. Câu hỏi mở cần xác nhận BA/PO

| # | Câu hỏi | Liên quan |
|---|---------|----------|
| Q-01 | UC1 Trang chủ đánh Out-of-scope trong WBS — có đúng không? Sidebar cần entry Home | Tree View |
| Q-02 | Nhắc hạn (UC229-243) gom vào Thông báo (UC258-259) — đúng ý BA? | Quyết định #8 |
| Q-03 | 4 nhóm AI Chatbot chưa rõ scope (Phiên tư vấn, An toàn, Gợi ý, Thu thập nhu cầu) — xác nhận In-scope? | Quyết định #9 |
| Q-04 | Bản đồ số (Tích hợp) — có trong roadmap phase nào? | Mapping Tích hợp |
| Q-05 | "Thông tin đã công bố" gom UC55-86 — sidebar chỉ hiện 1 entry, bên trong trang mới tách chi tiết? | Quyết định #4 |
| Q-06 | Nhóm "DỊCH VỤ" và "QUẢN LÝ XÚC TIẾN ĐẦU TƯ" có trùng lặp (đặt lịch, hồ sơ, PAKN) — giữ theo wireframe hay theo Excel? | Cấu trúc sidebar |
