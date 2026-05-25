# Assumptions & Best Practices — Sidebar Navigation (Cổng đầu tư Quốc gia trên Mobile)

**Tiêu đề:** Phân tích & Đề xuất cấu trúc Sidebar Mobile App  
**Ngày tạo:** 13/05/2026  
**Tác giả:** QC Agent  
**Phiên bản:** v1

---

## 1. Nhận xét Sidebar hiện tại

| Vấn đề | Mô tả |
|---------|--------|
| Quá nhiều mục KCN/KKT | 7 loại khu liệt kê riêng lẻ → gây rối, nên gom thành 1 entry + bộ lọc bên trong |
| Thiếu Trang chủ | Không có entry quay về Home |
| Thiếu AI Chatbot | Feature lớn nhưng không xuất hiện trong sidebar |
| Thiếu Bản đồ số | Feature quan trọng cho nhà đầu tư tra cứu vị trí |
| Thiếu Dashboard | UC list có Dashboard theo tài khoản nhưng sidebar không thể hiện |
| Không có Search | Sidebar dài nhưng không có thanh tìm kiếm nhanh |
| Flat quá mức | Tất cả ngang hàng, không phân biệt tần suất sử dụng |

---

## 2. Best Practices áp dụng

1. **Max 5–7 nhóm chính** — giảm cognitive load trên mobile
2. **Trang chủ luôn ở đầu** — anchor point cho user quay lại
3. **Gom các loại KCN/KKT thành 1 mục** — phân loại bằng filter/tab bên trong trang
4. **AI Chatbot = Floating Action Button (FAB)** — không nằm trong sidebar, luôn accessible
5. **Bản đồ số nằm trong nhóm KCN/KKT** — feature tra cứu trực quan, cần truy cập nhanh
6. **Nhóm theo hành trình người dùng** — Tìm hiểu → Tra cứu KCN → Nộp hồ sơ → Theo dõi
7. **Tách "Cài đặt" và "Đăng xuất" xuống footer cố định** — pattern chuẩn mobile

---

## 3. Lưu ý quan trọng

> **Assumption UX-03 (Đợt 1)** đã xác nhận: "Sidebar chứa toàn bộ menu (không có bottom nav bar)".  
> Do đó, đề xuất Bottom Tab Bar bên dưới là **gợi ý cải tiến UX**, cần xác nhận lại với BA/PO nếu muốn áp dụng.

---

## 4. Proposed Tree View — Sidebar Cổng đầu tư Mobile

```
┌─────────────────────────────────────────────────┐
│  [Avatar] Nguyễn Văn A                          │
│  nguyenvana@example.com                         │
│  Xem hồ sơ                                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  Trang chủ (Home)                               │
│  Dashboard (Dashboard cá nhân)                  │
│                                                 │
│  ── GIỚI THIỆU ──────────────────────────────  │
│  Giới thiệu (About)                            │
│  Lĩnh vực đầu tư (Investment Sectors)          │
│  Khu vực đầu tư (Investment Regions)           │
│  Liên hệ (Contact)                             │
│                                                 │
│  ── KHU CÔNG NGHIỆP & KHU KINH TẾ ──────────  │
│  Tra cứu KCN / KKT (Search IZ/EZ)             │
│     └─ [Bộ lọc bên trong trang:]              │
│        • Khu công nghiệp                       │
│        • KCN sinh thái                         │
│        • KCN công nghệ cao                     │
│        • Khu chế xuất                          │
│        • KCN hỗ trợ / chuyên ngành            │
│        • Khu kinh tế (ven biển/cửa khẩu/      │
│          chuyên biệt)                          │
│        • Khu phi thuế quan                     │
│        • Khu thương mại tự do                  │
│        • Mô hình khu khác                      │
│  Thông tin quỹ đất (Land Fund Info)            │
│  Bản đồ số (Digital Map)                       │
│                                                 │
│  ── DỊCH VỤ ĐẦU TƯ ─────────────────────────  │
│  Thủ tục hành chính (Admin Procedures)         │
│  Quản lý hồ sơ (Document Management)          │
│  Quản lý đặt lịch (Appointment Booking)       │
│  Báo cáo đầu tư (Investment Reports)          │
│  Phản ánh kiến nghị (Feedback/Complaints)      │
│                                                 │
│  ── TIN TỨC & TRA CỨU ──────────────────────  │
│  Tin tức (News)                                │
│  Văn bản pháp luật (Legal Documents)           │
│  Kho dữ liệu điện tử (Digital Repository)     │
│  FAQ                                           │
│  Hướng dẫn sử dụng (User Guide)               │
│                                                 │
│  ── XÚC TIẾN ĐẦU TƯ ────────────────────────  │
│  Thông tin xúc tiến (Promotion Info)           │
│  Nhắc hạn (Deadline Reminders)                 │
│                                                 │
├─────────────────────────────────────────────────┤
│  Cấu hình tài khoản (Account Settings)        │
│  Đăng xuất (Logout)                            │
└─────────────────────────────────────────────────┘

  ╔═══════════════════════════════════════════════╗
  ║  [FAB - Floating Action Button]              ║
  ║  AI Chatbot — luôn hiển thị góc phải dưới   ║
  ║  màn hình, không nằm trong sidebar           ║
  ╚═══════════════════════════════════════════════╝
```

---

## 5. Đề xuất Bottom Tab Bar (cần xác nhận BA/PO)

> Lưu ý: Assumption UX-03 hiện tại xác nhận KHÔNG có bottom nav bar.
> Phần này là gợi ý cải tiến, cần raise lên BA/PO để xác nhận.

```
┌──────┬──────────┬──────────┬──────────┬──────────┐
│ Home │ Bản đồ  │ Hồ sơ   │ Thông   │ Tài     │
│      │          │          │  báo    │ khoản   │
└──────┴──────────┴──────────┴──────────┴──────────┘
```

---

## 6. Bảng tổng hợp Assumptions

| # | Assumption | Lý do | Trạng thái |
|---|-----------|-------|------------|
| SB-01 | Gom tất cả loại KCN/KKT thành 1 mục "Tra cứu KCN/KKT" | Giảm từ 7 → 1 entry, phân loại bằng filter/tab trong trang chi tiết | Đề xuất — chờ BA |
| SB-02 | AI Chatbot là FAB, không nằm trong sidebar | Best practice: chatbot cần accessible mọi lúc, không bị ẩn sau hamburger menu | Đề xuất — chờ BA |
| SB-03 | Bản đồ số nằm trong nhóm KCN/KKT | Feature tra cứu trực quan, cần truy cập nhanh | Đề xuất — chờ BA |
| SB-04 | Dashboard cá nhân đặt ngay sau Trang chủ | Nhà đầu tư cần overview nhanh về hồ sơ, deadline, trạng thái | Đề xuất — chờ BA |
| SB-05 | Nhóm "Xúc tiến đầu tư" tách riêng | Phân biệt rõ giữa dịch vụ hành chính và thông tin xúc tiến | Đề xuất — chờ BA |
| SB-06 | Thứ tự nhóm theo user journey | Tìm hiểu → Tra cứu KCN → Nộp hồ sơ → Theo dõi → Tin tức | Đề xuất — chờ BA |
| SB-07 | Footer cố định cho Settings + Logout | Pattern chuẩn mobile, user không cần scroll xuống cuối để đăng xuất | Đề xuất — chờ BA |

---

## 7. Mapping Sidebar → UC

| Menu Item (đề xuất) | UC tương ứng | Nhóm |
|---|---|---|
| Trang chủ | UC1 | Header |
| Dashboard | UC1 (phần dashboard) | Header |
| Giới thiệu | UC86 | Giới thiệu |
| Lĩnh vực đầu tư | UC87-95 | Giới thiệu |
| Khu vực đầu tư | UC55 | Giới thiệu |
| Liên hệ | UC85 | Giới thiệu |
| Tra cứu KCN/KKT | UC2-31 | KCN & KKT |
| Thông tin quỹ đất | UC40 | KCN & KKT |
| Bản đồ số | (Chưa có UC riêng) | KCN & KKT |
| Thủ tục hành chính | UC73 | Dịch vụ đầu tư |
| Quản lý hồ sơ | UC45-51 | Dịch vụ đầu tư |
| Quản lý đặt lịch | UC42-44 | Dịch vụ đầu tư |
| Báo cáo đầu tư | UC54 | Dịch vụ đầu tư |
| Phản ánh kiến nghị | UC53, UC63-65 | Dịch vụ đầu tư |
| Tin tức | UC56-57, UC66, UC68 | Tin tức & Tra cứu |
| Văn bản pháp luật | UC69 | Tin tức & Tra cứu |
| Kho dữ liệu điện tử | UC52 | Tin tức & Tra cứu |
| FAQ | UC71-82 | Tin tức & Tra cứu |
| Hướng dẫn sử dụng | UC71-82 | Tin tức & Tra cứu |
| Thông tin xúc tiến | UC87-95 | Xúc tiến đầu tư |
| Nhắc hạn | (Thuộc UC258-259) | Xúc tiến đầu tư |
| AI Chatbot (FAB) | UC60-61 | Floating Button |
| Cấu hình tài khoản | UC249 | Footer |
| Đăng xuất | UC257 | Footer |
