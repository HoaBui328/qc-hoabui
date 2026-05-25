# Assumptions & Best Practices — Sidebar Navigation (Cổng đầu tư Quốc gia trên Mobile)

**Tiêu đề:** Phân tích & Đề xuất cấu trúc Sidebar Mobile App  
**Ngày tạo:** 13/05/2026  
**Tác giả:** QC Agent  
**Phiên bản:** v2  
**Nguồn dữ liệu:** [MBFS - Cổng đầu tư QG] BA internal file .xlsx — Sheet "WBS (Mobile)", "Internal QnA (Mobile)"

---

## 1. Nhận xét Sidebar hiện tại (từ wireframe)

| # | Vấn đề | Mô tả | Mức độ |
|---|--------|-------|--------|
| 1 | Quá nhiều mục KCN/KKT | 7 loại khu liệt kê riêng lẻ → gây cognitive overload | 🔴 Cao |
| 2 | Thiếu Trang chủ (Home) | Không có entry quay về Home — vi phạm anchor point pattern | 🔴 Cao |
| 3 | Thiếu AI Chatbot | Feature lớn (UC60-61) nhưng không xuất hiện trong sidebar | 🟡 TB |
| 4 | Thiếu Bản đồ số | Feature quan trọng cho NĐT tra cứu vị trí KCN/KKT | 🟡 TB |
| 5 | Thiếu Dashboard | WBS có nhóm Dashboard (UC244-248) In-scope nhưng sidebar không thể hiện | 🔴 Cao |
| 6 | Thiếu nhóm Nhắc hạn | WBS có nhóm Nhắc hạn (UC229-243) In-scope nhưng sidebar không có | 🔴 Cao |
| 7 | Thiếu Tra cứu chuyên sâu | UC58, UC59, UC62 In-scope nhưng sidebar gộp chung | 🟡 TB |
| 8 | Flat quá mức | Tất cả menu items ngang hàng, không phân biệt tần suất sử dụng | 🟡 TB |
| 9 | Không có Search | Sidebar dài nhưng không có thanh tìm kiếm nhanh | 🟢 Thấp |

---

## 2. Best Practices áp dụng cho Mobile Sidebar

| # | Nguyên tắc | Áp dụng | Nguồn |
|---|-----------|---------|-------|
| BP-01 | **Max 5–7 nhóm chính** | Gom KCN/KKT thành 1, tách nhóm rõ ràng | Material Design 3 |
| BP-02 | **Trang chủ luôn ở đầu** | Thêm "Trang chủ" ngay dưới profile | iOS HIG |
| BP-03 | **Gom danh mục lớn thành 1 entry** | 7 loại KCN/KKT → 1 entry + filter/tab | Google Maps pattern |
| BP-04 | **AI Chatbot = FAB** | Không nằm trong sidebar, luôn accessible | Material Design FAB |
| BP-05 | **Nhóm theo hành trình người dùng** | Tìm hiểu → Tra cứu → Nộp hồ sơ → Theo dõi | UX journey mapping |
| BP-06 | **Footer cố định cho Settings + Logout** | User không cần scroll xuống cuối | Standard drawer |
| BP-07 | **Badge/count trên menu item** | Badge thông báo, số hồ sơ chờ | iOS notification badge |

---

## 3. Lưu ý quan trọng

> **Assumption UX-03 (Đợt 1):** "Sidebar chứa toàn bộ menu (không có bottom nav bar)".  
> Đề xuất Bottom Tab Bar là **gợi ý cải tiến UX**, cần xác nhận BA/PO.

> **Nguồn dữ liệu:** UC ID được đối chiếu từ sheet "WBS (Mobile)". Chỉ UC **In-scope** được đưa vào tree view.

---

## 4. Proposed Tree View — Sidebar Cổng đầu tư Mobile

```
┌─────────────────────────────────────────────────┐
│  [Avatar] Nguyễn Văn A                          │
│  nguyenvana@example.com                         │
│  Xem hồ sơ → UC249                             │
├─────────────────────────────────────────────────┤
│                                                 │
│  🏠 Trang chủ (Home) → UC1                     │
│  📊 Dashboard (Personal) → UC244-248           │
│                                                 │
│  ── GIỚI THIỆU ──────────────────────────────  │
│  ℹ️  Giới thiệu (About) → UC86                │
│  📋 Lĩnh vực đầu tư → UC87-95                 │
│  🗺️  Khu vực đầu tư → UC55                     │
│  📞 Liên hệ (Contact) → UC85                  │
│                                                 │
│  ── KHU CÔNG NGHIỆP & KHU KINH TẾ ──────────  │
│  🔍 Tra cứu KCN / KKT → UC2-31                │
│     └─ [Bộ lọc/Tab bên trong trang:]          │
│        • Khu công nghiệp (UC2-6)               │
│        • KCN sinh thái (UC7-11)                │
│        • Khu thương mại tự do (UC27-31)        │
│        • Mô hình khu khác (UC32-39)            │
│  📐 Thông tin quỹ đất → UC40                   │
│  🗺️  Bản đồ số → Chưa có UC                    │
│                                                 │
│  ── DỊCH VỤ ĐẦU TƯ ─────────────────────────  │
│  📝 Thủ tục hành chính → UC70                  │
│  📁 Quản lý hồ sơ → UC45-51                   │
│  📅 Quản lý đặt lịch → UC42-44                │
│  📊 Báo cáo đã nộp → UC54                     │
│  💬 Phản ánh kiến nghị → UC53, UC63-65         │
│  ⏰ Nhắc hạn → UC229-243                       │
│                                                 │
│  ── TRA CỨU ─────────────────────────────────  │
│  🏢 Tra cứu thủ tục đầu tư → UC58             │
│  📈 Tra cứu báo cáo đầu tư → UC59             │
│  🤝 Tra cứu DN kết nối đối tác → UC62         │
│                                                 │
│  ── TIN TỨC & HỖ TRỢ ───────────────────────  │
│  📰 Tin tức → UC56-57, UC66, UC68              │
│  📜 Văn bản pháp luật → UC69                   │
│  📂 Kho dữ liệu điện tử → UC52                │
│  ❓ FAQ → UC76-82                               │
│  📖 Hướng dẫn sử dụng → UC71-75               │
│                                                 │
│  ── XÚC TIẾN ĐẦU TƯ ────────────────────────  │
│  🎯 Dự án kêu gọi đầu tư → UC87              │
│  📄 VB thông báo tổ chức XTĐT → UC93          │
│                                                 │
├─────────────────────────────────────────────────┤
│  ⚙️  Cấu hình tài khoản → UC249               │
│  🚪 Đăng xuất → UC257                         │
└─────────────────────────────────────────────────┘

  ╔═══════════════════════════════════════════════╗
  ║  [FAB] 🤖 AI Chatbot → UC60-61              ║
  ║  Luôn hiển thị góc phải dưới màn hình       ║
  ╚═══════════════════════════════════════════════╝
```

### Thay đổi so với v1

| # | Thay đổi | Lý do |
|---|---------|-------|
| 1 | Thêm nhóm **"Tra cứu"** cho UC58, UC59, UC62 | WBS xác nhận In-scope |
| 2 | Thêm **"Nhắc hạn"** vào Dịch vụ | WBS: UC229-243 (15 UC) In-scope |
| 3 | Cập nhật UC70 cho TTHC | Đối chiếu WBS |
| 4 | Tách **Xúc tiến ĐT** — chỉ giữ UC87 + UC93 | UC88-91, UC94-95 Out-of-scope |
| 5 | Ghi chú OOS cho KKT, PTQ | WBS xác nhận |
| 6 | Tách UC54 (đã nộp) vs UC59 (tra cứu) | Phân biệt rõ 2 chức năng |

---

## 5. Bảng tổng hợp Assumptions

| # | Assumption | Lý do | Nguồn WBS | Trạng thái |
|---|-----------|-------|-----------|------------|
| SB-01 | Gom KCN/KKT thành 1 mục + filter/tab | Giảm 7 → 1 entry | UC2-31 cùng nhóm | Đề xuất — chờ BA |
| SB-02 | AI Chatbot là FAB | Cần accessible mọi lúc | UC60-61, QnA #30-46 | Đề xuất — chờ BA |
| SB-03 | Bản đồ số trong nhóm KCN/KKT | Tra cứu trực quan | Chưa có UC riêng | Đề xuất — chờ BA |
| SB-04 | Dashboard ngay sau Trang chủ | 5 UC Dashboard In-scope | UC244-248 (R325-329) | Đề xuất — chờ BA |
| SB-05 | Nhóm "Tra cứu" riêng cho UC58,59,62 | 3 UC chuyên sâu In-scope | R109-113 | Đề xuất — chờ BA |
| SB-06 | Thêm "Nhắc hạn" vào Dịch vụ | 15 UC nhắc hạn In-scope | UC229-243 (R310-324) | Đề xuất — chờ BA |
| SB-07 | Xúc tiến ĐT chỉ giữ UC87 + UC93 | UC88-91, 94-95 OOS/Cancel | R156-176 | Đề xuất — chờ BA |
| SB-08 | Thứ tự theo user journey | UX best practice | — | Đề xuất — chờ BA |
| SB-09 | Footer cố định Settings + Logout | Standard mobile drawer | Material Design | Đề xuất — chờ BA |
| SB-10 | KKT/PTQ hiển thị "Sắp ra mắt" | OOS nhưng giữ placeholder | UC12-16, UC22-26 | Đề xuất — chờ BA |

---

## 6. Mapping Sidebar → UC (In-scope)

| # | Menu Item | UC IDs | Nhóm | Scope |
|---|----------|--------|------|-------|
| 1 | Trang chủ | UC1 | Header | OOS (*) |
| 2 | Dashboard | UC244-248 | Header | In-scope |
| 3 | Giới thiệu | UC86 | Giới thiệu | In-scope |
| 4 | Lĩnh vực đầu tư | UC87-95 | Giới thiệu | Hỗn hợp |
| 5 | Khu vực đầu tư | UC55 | Giới thiệu | In-scope |
| 6 | Liên hệ | UC85 | Giới thiệu | In-scope |
| 7 | Tra cứu KCN/KKT | UC2-6, 7-11, 27-31, 32-39 | KCN & KKT | In-scope |
| 8 | Thông tin quỹ đất | UC40 | KCN & KKT | In-scope |
| 9 | Bản đồ số | (Chưa có UC) | KCN & KKT | TBD |
| 10 | Thủ tục hành chính | UC70 | Dịch vụ | In-scope |
| 11 | Quản lý hồ sơ | UC45-51 | Dịch vụ | In-scope |
| 12 | Quản lý đặt lịch | UC42-44 | Dịch vụ | In-scope |
| 13 | Báo cáo đã nộp | UC54 | Dịch vụ | In-scope |
| 14 | Phản ánh kiến nghị | UC53, 63-65 | Dịch vụ | In-scope |
| 15 | Nhắc hạn | UC229-243 | Dịch vụ | In-scope |
| 16 | Tra cứu thủ tục ĐT | UC58 | Tra cứu | In-scope |
| 17 | Tra cứu báo cáo ĐT | UC59 | Tra cứu | In-scope |
| 18 | Tra cứu DN kết nối | UC62 | Tra cứu | In-scope |
| 19 | Tin tức | UC56-57, 66, 68 | Tin tức | In-scope |
| 20 | Văn bản pháp luật | UC69 | Tin tức | In-scope |
| 21 | Kho dữ liệu ĐT | UC52 | Tin tức | In-scope |
| 22 | FAQ | UC76-82 | Tin tức | In-scope |
| 23 | Hướng dẫn sử dụng | UC71-75 | Tin tức | In-scope |
| 24 | Dự án kêu gọi ĐT | UC87 | Xúc tiến | In-scope |
| 25 | VB thông báo XTĐT | UC93 | Xúc tiến | In-scope |
| 26 | AI Chatbot (FAB) | UC60-61 | FAB | In-scope |
| 27 | Cấu hình tài khoản | UC249-254 | Footer | In-scope |
| 28 | Đăng xuất | UC257 | Footer | In-scope |

> (*) UC1 Trang chủ: WBS đánh Out-of-scope nhưng là entry point cần thiết → cần xác nhận BA.

---

## 7. UC In-scope CHƯA có trên Sidebar hiện tại

| # | Nhóm | UC IDs | Số UC | Ghi chú |
|---|------|--------|-------|---------|
| 1 | Nhắc hạn | UC229-243 | 15 | Hoàn toàn thiếu |
| 2 | Dashboard | UC244-248 | 5 | Hoàn toàn thiếu |
| 3 | Tra cứu thủ tục ĐT | UC58 | 1 | Thiếu entry riêng |
| 4 | Tra cứu báo cáo ĐT | UC59 | 1 | Thiếu entry riêng |
| 5 | Tra cứu DN kết nối | UC62 | 1 | Hoàn toàn thiếu |
| 6 | Dự án ĐT KCN/KKT | UC32-39 | 8 | Thiếu entry riêng |
| 7 | Thông báo hệ thống | UC258-259 | 2 | → Icon bell trên header |

---

## 8. Câu hỏi mở cần xác nhận BA/PO

| # | Câu hỏi | Liên quan |
|---|---------|----------|
| Q-01 | UC1 Trang chủ đánh OOS — có đúng không? | Tree View |
| Q-02 | Nhắc hạn (15 UC) nằm trong Dịch vụ hay tách riêng? | SB-06 |
| Q-03 | Dashboard là sub-page Trang chủ hay entry riêng? | SB-04 |
| Q-04 | KKT/PTQ đang OOS — giữ placeholder không? | SB-10 |
| Q-05 | Bản đồ số có trong roadmap không? | SB-03 |
| Q-06 | "Báo cáo đầu tư" = UC54 hay UC59 hay cả hai? | Mapping #13, #17 |
