# Assumptions & Best Practices — Sidebar Navigation (Cổng đầu tư Quốc gia trên Mobile)

**Tiêu đề:** Phân tích & Đề xuất cấu trúc Sidebar Mobile App  
**Ngày tạo:** 14/05/2026  
**Tác giả:** QC Agent  
**Phiên bản:** v4 (Final)  
**Nguồn dữ liệu:** [MBFS - Cổng đầu tư QG] BA internal file .xlsx — Sheet "WBS (Mobile)"

---

## 1. Quyết định đã thống nhất (Q&A 13-14/05/2026)

| # | Hạng mục | Quyết định |
|---|----------|-----------|
| 1 | Scope hiển thị | **TẤT CẢ** tính năng (In-scope + Out-of-scope + Cancel) đều đưa vào sidebar |
| 2 | Cấu trúc danh mục | Theo đúng **6 danh mục Excel** (bỏ nhóm GIỚI THIỆU, DỊCH VỤ riêng của wireframe) |
| 3 | KCN/KKT (16 nhóm) | Gom thành 1 mục + bộ lọc bên trong trang |
| 4 | Quản lý Xúc tiến ĐT | Giữ 1 nhóm duy nhất (đúng như Excel) |
| 5 | UC55-86 "Khai thác TT đã công bố" | Gom thành 1 mục "Thông tin đã công bố" |
| 6 | AI Chatbot | 1 mục trong sidebar (KHÔNG phải FAB) |
| 7 | Trang chủ | Có mục riêng đầu sidebar (bao gồm Dashboard) |
| 8 | Dashboard theo tài khoản | Gom vào Trang chủ |
| 9 | Nhắc hạn | Gom vào Thông báo (UC258-259) |
| 10 | Nhóm chưa rõ scope | Xác nhận In-scope, đưa vào sidebar |
| 11 | Cấu trúc sidebar | Flat với section header |
| 12 | Thứ tự | Theo wireframe hiện tại |
| 13 | Trùng lặp | Tối ưu hoá, ưu tiên Excel. Nếu trùng → gom lại |
| 14 | Cancel items | Vẫn đưa vào sidebar (gom vào bộ lọc hoặc mục phù hợp) |
| 15 | Bản đồ số | Đưa vào sidebar, gợi ý vị trí best practice |

---

## 2. Proposed Tree View — Sidebar (v4 Final)

```
┌─────────────────────────────────────────────────┐
│  [Avatar] Nguyễn Văn A                          │
│  nguyenvana@example.com                         │
│  Xem hồ sơ                                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  Trang chủ (bao gồm Dashboard)                 │
│                                                 │
│  ── KHU CÔNG NGHIỆP / KKT ──────────────────  │
│  Tra cứu KCN / KKT                            │
│     └─ [Bộ lọc bên trong trang:]              │
│        • Khu công nghiệp                       │
│        • Khu chế xuất                          │
│        • KCN hỗ trợ                            │
│        • KCN chuyên ngành                      │
│        • KCN sinh thái                         │
│        • KCN công nghệ cao                     │
│        • Khu kinh tế                           │
│        • Khu kinh tế ven biển                  │
│        • Khu kinh tế cửa khẩu                 │
│        • Khu kinh tế chuyên biệt              │
│        • Khu phi thuế quan                     │
│        • Khu thương mại tự do                  │
│        • Mô hình khu khác                      │
│  Tra cứu tổng hợp KCN/KKT                     │
│  Dự án đầu tư KCN/KKT                         │
│  Kiểm tra KCN/KKT                             │
│     └─ Thông tin quỹ đất                      │
│     └─ Cho thuê đất trong KCN                 │
│                                                 │
│  ── QUẢN LÝ XÚC TIẾN ĐẦU TƯ ───────────────  │
│  Quản lý đặt lịch nộp thủ tục                 │
│  Quản lý hồ sơ                                 │
│  Tra cứu kho dữ liệu điện tử                  │
│  Tra cứu phản ánh kiến nghị                   │
│  Tra cứu báo cáo NĐT đã nộp                   │
│  Thông tin đã công bố                          │
│     └─ [Bên trong trang:]                     │
│        • Chuyên trang đầu tư theo khu vực     │
│        • Tin tức lĩnh vực đầu tư              │
│        • Tin tức chính sách đầu tư            │
│        • Thủ tục đầu tư                       │
│        • Báo cáo đầu tư                       │
│        • Chatbot (UC60-61)                     │
│        • DN kết nối đối tác                    │
│        • PAKN (xem, tạo, tra cứu trạng thái) │
│        • Tin tức đầu tư / DVC / Câu chuyện    │
│        • Văn bản pháp luật                     │
│        • Thủ tục hành chính                    │
│        • Hướng dẫn sử dụng                    │
│        • FAQ                                   │
│        • Điều khoản sử dụng                   │
│        • Chính sách bảo mật                   │
│        • Liên hệ                               │
│        • Giới thiệu Cục ĐTNN                  │
│  Khai thác thông tin xúc tiến đầu tư          │
│     └─ [Bên trong trang:]                     │
│        • Dự án kêu gọi đầu tư                 │
│        • Chương trình XTĐT (QG/Bộ ngành/ĐP)  │
│        • Văn bản thỏa thuận MOU               │
│        • Hồ sơ đầu tư cá nhân/tổ chức        │
│        • VB thông báo tổ chức XTĐT            │
│        • Danh mục dự án ĐT bộ ngành/ĐP       │
│                                                 │
│  ── AI CHATBOT & CÁ NHÂN HOÁ ───────────────  │
│  AI Chatbot                                    │
│     └─ [16 knowledge domains bên trong:]      │
│        • Quy định chung                        │
│        • Ngành nghề & tiếp cận thị trường     │
│        • Ưu đãi & hỗ trợ đầu tư              │
│        • Hồ sơ & thủ tục đầu tư              │
│        • Triển khai & chấp thuận dự án        │
│        • Nghĩa vụ tài chính & ký quỹ         │
│        • Triển khai & vận hành dự án          │
│        • Điều chỉnh dự án                     │
│        • Chuyển nhượng & tái cấu trúc        │
│        • Chấm dứt dự án                       │
│        • Quản lý nhà nước & xúc tiến         │
│        • Báo cáo & giám sát                   │
│        • Chuyển tiếp & trường hợp đặc biệt   │
│        • Đầu tư ra nước ngoài                 │
│        • Đa ngôn ngữ                          │
│        • Đánh giá câu trả lời                 │
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

## 3. Mapping chi tiết Sidebar → Excel WBS

### 3.1 TRANG CHỦ

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| Trang chủ | Chứa các đường dẫn nhanh... | UC1 | Bao gồm Dashboard (UC244-248) |

### 3.2 KHU CÔNG NGHIỆP / KKT

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| Tra cứu KCN/KKT (bộ lọc: KCN) | Khai thác thông tin khu công nghiệp | UC2-6 | In scope |
| *(bộ lọc: Khu chế xuất)* | Khai thác thông tin khu chế xuất | — | Cancel → vẫn hiện trong bộ lọc |
| *(bộ lọc: KCN hỗ trợ)* | Khai thác thông tin KCN hỗ trợ | — | Cancel → vẫn hiện |
| *(bộ lọc: KCN chuyên ngành)* | Khai thác thông tin KCN chuyên ngành | — | Cancel → vẫn hiện |
| *(bộ lọc: KCN sinh thái)* | Khai thác thông tin KCN sinh thái | UC17-21 | In scope |
| *(bộ lọc: KCN công nghệ cao)* | Khai thác thông tin KCN công nghệ cao | — | Cancel → vẫn hiện |
| *(bộ lọc: Khu kinh tế)* | Khai thác thông tin khu kinh tế | UC7-11 | Out-of-scope |
| *(bộ lọc: KKT ven biển)* | Khai thác thông tin KKT ven biển | — | Cancel → vẫn hiện |
| *(bộ lọc: KKT cửa khẩu)* | Khai thác thông tin KKT cửa khẩu | — | Cancel → vẫn hiện |
| *(bộ lọc: KKT chuyên biệt)* | Khai thác thông tin KKT chuyên biệt | — | Cancel → vẫn hiện |
| *(bộ lọc: Khu phi thuế quan)* | Khai thác thông tin khu phi thuế quan | UC22-26 | Out-of-scope |
| *(bộ lọc: Khu TMTD)* | Khai thác thông tin khu thương mại tự do | UC27-31 | In scope |
| *(bộ lọc: Mô hình khu khác)* | Khai thác thông tin mô hình khu khác | UC12-16 | Out-of-scope |
| Tra cứu tổng hợp KCN/KKT | Tra cứu tổng hợp thông tin các KCN/KKT | — | Cancel → vẫn hiện |
| Dự án đầu tư KCN/KKT | Khai thác thông tin dự án đầu tư KCN/KKT | UC32-39 | In scope |
| Kiểm tra KCN/KKT | Khai thác thông tin kiểm tra KCN, KTT | UC40-41 | Out-of-scope |

### 3.3 QUẢN LÝ XÚC TIẾN ĐẦU TƯ TRÊN MOBILE

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| Quản lý đặt lịch nộp thủ tục | Quản lý đặt lịch nộp thủ tục về đầu tư | UC42-44 | In scope |
| Quản lý hồ sơ | Quản lý hồ sơ trên mobile | UC45-51 | In scope |
| Tra cứu kho dữ liệu điện tử | Tra cứu kho dữ liệu điện tử trên mobile | UC52 | In scope |
| Tra cứu phản ánh kiến nghị | Tra cứu phản ánh kiến nghị trên mobile | UC53, 63-65 | In scope |
| Tra cứu báo cáo NĐT đã nộp | Tra cứu báo cáo nhà đầu tư đã nộp | UC54 | In scope |
| Thông tin đã công bố | Khai thác thông tin đã công bố trên mobile | UC55-86 | In scope (gom) |
| Khai thác TT xúc tiến đầu tư | Khai thác thông tin xúc tiến đầu tư | UC87-95 | Hỗn hợp |

### 3.4 AI CHATBOT & CÁ NHÂN HOÁ HỖ TRỢ NHÀ ĐẦU TƯ

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| AI Chatbot | Gom 16 knowledge domains | UC60-61, UC96-228 | 1 entry, domains bên trong |
| — Quy định chung | Quy định chung | UC96-105 | Out-of-scope |
| — Ngành nghề & tiếp cận thị trường | Ngành nghề và tiếp cận thị trường | UC106-117 | Out-of-scope |
| — Ưu đãi & hỗ trợ đầu tư | Ưu đãi và hỗ trợ đầu tư | UC118-129 | Out-of-scope |
| — Hồ sơ & thủ tục đầu tư | Hồ sơ và thủ tục đầu tư | UC130-144 | Out-of-scope |
| — Triển khai & chấp thuận dự án | Triển khai và chấp thuận dự án | UC145-156 | Out-of-scope |
| — Nghĩa vụ tài chính & ký quỹ | Nghĩa vụ tài chính & ký quỹ | UC157-164 | Out-of-scope |
| — Triển khai & vận hành dự án | Triển khai và vận hành dự án | UC165-172 | Out-of-scope |
| — Điều chỉnh dự án | Điều chỉnh dự án | UC173-182 | Out-of-scope |
| — Chuyển nhượng & tái cấu trúc | Chuyển nhượng và tái cấu trúc | UC183-190 | Out-of-scope |
| — Chấm dứt dự án | Chấm dứt dự án | UC191-196 | Out-of-scope |
| — Quản lý nhà nước & xúc tiến | Quản lý nhà nước và xúc tiến | UC197-202 | Out-of-scope |
| — Báo cáo & giám sát | Báo cáo và giám sát | UC203-207 | Out-of-scope |
| — Chuyển tiếp & trường hợp đặc biệt | Chuyển tiếp và trường hợp đặc biệt | UC208-212 | Out-of-scope |
| — Đầu tư ra nước ngoài | Đầu tư ra nước ngoài | UC213-222 | Out-of-scope |
| — Đa ngôn ngữ | Đa ngôn ngữ | UC223-227 | Out-of-scope |
| — Đánh giá câu trả lời | Đánh giá câu trả lời | UC228 | Out-of-scope |
| Nhắc hạn *(→ gom vào Thông báo)* | Nhắc hạn trên mobile | UC229-243 | In scope |
| Dashboard *(→ gom vào Trang chủ)* | Dashboard theo tài khoản trên mobile | UC244-248 | In scope |
| Quản lý phiên tư vấn & lịch sử | Quản lý phiên tư vấn, lịch sử và tài liệu đầu ra | — | In scope (xác nhận) |
| An toàn, giới hạn & kết nối hỗ trợ | An toàn, giới hạn tư vấn và kết nối hỗ trợ | — | In scope (xác nhận) |
| Gợi ý & so sánh phương án ĐT | Gợi ý và so sánh phương án đầu tư | — | In scope (xác nhận) |
| Thu thập nhu cầu & cá nhân hoá | Thu thập nhu cầu và cá nhân hoá tư vấn cho NĐT | — | In scope (xác nhận) |

### 3.5 QUẢN LÝ CHUNG TRÊN MOBILE

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| Quản lý tài khoản NĐT | Quản lý tài khoản nhà đầu tư trên mobile | UC249-255 | In scope |
| Thông báo hệ thống | Quản lý thông tin chung (phần thông báo) | UC258-259 | In scope, bao gồm Nhắc hạn |
| Đăng nhập | Quản lý thông tin chung (phần đăng nhập) | UC256 | In scope |
| Đăng xuất | Quản lý thông tin chung (phần đăng xuất) | UC257 | In scope |
| Cấu hình tài khoản | Quản lý tài khoản (phần cấu hình) | UC254, UC260 | In scope |

### 3.6 TÍCH HỢP

| Menu Item | Nhóm chức năng (Excel) | UC IDs | Ghi chú |
|---|---|---|---|
| Bản đồ số | Bản đồ số trên mobile | — | In scope (xác nhận). Best practice: đặt trong QUẢN LÝ CHUNG hoặc KCN/KKT vì liên quan tra cứu vị trí |

---

## 4. Thống kê coverage

| Danh mục (Excel) | Tổng nhóm chức năng | Hiển thị trên Sidebar | Gom vào bộ lọc/sub-page | Ghi chú |
|---|---|---|---|---|
| Trang chủ | 1 | 1 mục | — | Dashboard gom vào |
| KCN/KKT | 16 | 4 mục | 13 bộ lọc | Gom loại khu vào 1 entry |
| Quản lý Xúc tiến ĐT | 7 | 7 mục | UC55-86 gom bên trong | — |
| AI Chatbot & Cá nhân hoá | 22 | 5 mục | 16 knowledge domains | Nhắc hạn → Thông báo, Dashboard → Trang chủ |
| Quản lý chung | 2 | 5 mục | — | Tách ĐN/ĐX/Thông báo/Cấu hình |
| Tích hợp | 1 | 1 mục | — | Bản đồ số |
| **TỔNG** | **49** | **23 mục sidebar** | **29+ sub-items** | **100% coverage** |

---

## 5. Best Practice Notes

| # | Gợi ý | Áp dụng |
|---|-------|---------|
| 1 | Bản đồ số đặt trong nhóm **QUẢN LÝ CHUNG** | Vì là tính năng cross-cutting, hỗ trợ tra cứu KCN/KKT + dự án + quỹ đất trên bản đồ |
| 2 | Items Cancel hiển thị với badge "Sắp ra mắt" hoặc disabled state | Để user biết tính năng sẽ có nhưng chưa khả dụng |
| 3 | "Thông tin đã công bố" nên có icon expand/collapse | Vì chứa nhiều sub-features (UC55-86) |
| 4 | Thông báo nên có badge count (số chưa đọc) | Bao gồm cả nhắc hạn |
| 5 | AI Chatbot nên có indicator trạng thái (online/offline) | UX pattern cho chatbot |
| 6 | Footer (Cấu hình + Đăng xuất) luôn cố định cuối sidebar | Không bị scroll mất |

---

## 6. Design Update Spec — Bổ sung sub-items trên wireframe (14/05/2026)

> Mục đích: Wireframe hiện tại thiếu sub-items ở một số mục. Dưới đây là danh sách cần bổ sung để design khớp 100% với file MD v4.

### 6.1 "Thông tin đã công bố" — Bổ sung 13 sub-items

**Hiện tại trên design (4 items):**
- Tin tức & Chuyên trang
- Thủ tục & Hành chính
- Báo cáo đầu tư
- Văn bản pháp luật

**Cần cập nhật thành (17 items, expand đầy đủ):**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Chuyên trang đầu tư theo khu vực | UC55 | — |
| 2 | Tin tức lĩnh vực đầu tư | UC56 | — |
| 3 | Tin tức chính sách đầu tư | UC57 | — |
| 4 | Thủ tục đầu tư | UC58 | — |
| 5 | Báo cáo đầu tư | UC59 | — |
| 6 | Chatbot | UC60-61 | — |
| 7 | DN kết nối đối tác | UC62 | — |
| 8 | PAKN (xem, tạo, tra cứu trạng thái) | UC63-65 | — |
| 9 | Tin tức đầu tư / DVC / Câu chuyện thành công | UC66-68 | — |
| 10 | Văn bản pháp luật | UC69 | — |
| 11 | Thủ tục hành chính | UC70 | — |
| 12 | Hướng dẫn sử dụng | UC71-75 | — |
| 13 | FAQ | UC76-82 | — |
| 14 | Điều khoản sử dụng | UC83 | — |
| 15 | Chính sách bảo mật | UC84 | — |
| 16 | Liên hệ | UC85 | — |
| 17 | Giới thiệu Cục ĐTNN | UC86 | — |

### 6.2 "Khai thác thông tin xúc tiến đầu tư" — Expand 6 sub-items

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand:**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Dự án kêu gọi đầu tư | UC87 | In scope |
| 2 | Chương trình XTĐT Quốc gia | UC88 | Out-of-scope |
| 3 | Chương trình XTĐT Bộ ngành | UC89 | Out-of-scope |
| 4 | Chương trình XTĐT Địa phương | UC90 | Out-of-scope |
| 5 | Văn bản thỏa thuận hợp tác MOU | UC91 | Out-of-scope |
| 6 | Hồ sơ đầu tư cá nhân/tổ chức | UC92 | Out-of-scope |
| 7 | VB thông báo tổ chức hoạt động XTĐT | UC93 | In scope |
| 8 | Danh mục dự án ĐT bộ ngành | UC94 | Out-of-scope |
| 9 | Danh mục dự án ĐT địa phương | UC95 | Out-of-scope |

### 6.3 "Kiểm tra KCN/KKT" — Expand 2 sub-items

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand:**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Thông tin quỹ đất | UC40 | Out-of-scope |
| 2 | Cho thuê đất trong KCN | UC41 | Out-of-scope |

### 6.4 "Tra cứu tổng hợp KCN/KKT" — Expand 2 sub-items

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand:**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Theo dõi hồ sơ các KCN/KKT | — | Cancel |
| 2 | Tra cứu tổng hợp thông tin các KCN/KKT | — | Cancel |

### 6.5 "Dự án đầu tư KCN/KKT" — Expand 8 sub-items

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand:**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Tra cứu TT dự án ĐT xây dựng & kinh doanh kết cấu hạ tầng KCN | UC32 | In scope |
| 2 | Theo dõi lịch sử cập nhật TT dự án ĐT XD&KD kết cấu HT KCN | UC33 | In scope |
| 3 | Tra cứu TT dự án ĐT sản xuất kinh doanh trong KCN | UC34 | In scope |
| 4 | Theo dõi lịch sử cập nhật TT dự án ĐT SXKD trong KCN | UC35 | In scope |
| 5 | Tra cứu TT dự án ĐT XD&KD kết cấu HT KKT | UC36 | In scope |
| 6 | Theo dõi lịch sử cập nhật TT dự án ĐT XD&KD kết cấu HT KKT | UC37 | In scope |
| 7 | Tra cứu TT dự án ĐT SXKD trong KKT | UC38 | In scope |
| 8 | Theo dõi lịch sử cập nhật TT dự án ĐT SXKD trong KKT | UC39 | In scope |

### 6.6 "AI Chatbot" — 16 knowledge domains (đã có trong MD, design chưa expand)

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand (khi user tap vào AI Chatbot):**

| # | Knowledge Domain | UC IDs |
|---|-----------------|--------|
| 1 | Quy định chung | UC96-105 |
| 2 | Ngành nghề & tiếp cận thị trường | UC106-117 |
| 3 | Ưu đãi & hỗ trợ đầu tư | UC118-129 |
| 4 | Hồ sơ & thủ tục đầu tư | UC130-144 |
| 5 | Triển khai & chấp thuận dự án | UC145-156 |
| 6 | Nghĩa vụ tài chính & ký quỹ | UC157-164 |
| 7 | Triển khai & vận hành dự án | UC165-172 |
| 8 | Điều chỉnh dự án | UC173-182 |
| 9 | Chuyển nhượng & tái cấu trúc | UC183-190 |
| 10 | Chấm dứt dự án | UC191-196 |
| 11 | Quản lý nhà nước & xúc tiến | UC197-202 |
| 12 | Báo cáo & giám sát | UC203-207 |
| 13 | Chuyển tiếp & trường hợp đặc biệt | UC208-212 |
| 14 | Đầu tư ra nước ngoài | UC213-222 |
| 15 | Đa ngôn ngữ | UC223-227 |
| 16 | Đánh giá câu trả lời | UC228 |

### 6.7 "Thông báo hệ thống" — Expand sub-items (Nhắc hạn)

**Hiện tại trên design:** Không hiển thị sub-items

**Cần expand:**

| # | Sub-item | UC IDs | Ghi chú |
|---|----------|--------|---------|
| 1 | Thông báo hệ thống | UC258 | In scope |
| 2 | Thông báo kết quả xử lý hồ sơ | UC259 | In scope |
| 3 | Nhắc hạn bổ sung hồ sơ | UC229 | In scope |
| 4 | Nhắc hạn báo cáo định kỳ | UC230 | In scope |
| 5 | Nhắc hạn nghĩa vụ tài chính | UC231 | In scope |
| 6 | Nhắc hạn điều chỉnh dự án | UC232 | In scope |
| 7 | Nhắc hạn gia hạn dự án | UC233 | In scope |
| 8 | Nhắc hạn nghĩa vụ pháp lý phát sinh | UC234 | In scope |
| 9 | Cảnh báo quá hạn | UC235 | In scope |
| 10 | Tổng hợp lịch nghĩa vụ | UC236 | In scope |
| 11 | Lịch sử nhắc hạn | UC237 | In scope |
| 12 | Cá nhân hóa nhắc hạn | UC238 | In scope |
| 13 | Nhắc hạn theo loại dự án | UC239 | In scope |
| 14 | Nhắc hạn theo địa bàn | UC240 | In scope |
| 15 | Nhắc hạn theo ngành | UC241 | In scope |
| 16 | Báo cáo tuân thủ nghĩa vụ | UC242 | In scope |
| 17 | Tra cứu tiền lệ tương tự | UC243 | In scope |

---

## 7. Tổng hợp thay đổi cần thực hiện trên Design

| # | Mục | Hành động | Số items bổ sung |
|---|-----|-----------|-----------------|
| 1 | Thông tin đã công bố | Thay 4 items → 17 items đầy đủ | +13 |
| 2 | Khai thác TT xúc tiến ĐT | Expand sub-items | +9 |
| 3 | Kiểm tra KCN/KKT | Expand sub-items | +2 |
| 4 | Tra cứu tổng hợp KCN/KKT | Expand sub-items | +2 |
| 5 | Dự án đầu tư KCN/KKT | Expand sub-items | +8 |
| 6 | AI Chatbot | Expand 16 knowledge domains | +16 |
| 7 | Thông báo hệ thống | Expand (thông báo + nhắc hạn) | +17 |
| **TỔNG** | | | **+67 sub-items** |
