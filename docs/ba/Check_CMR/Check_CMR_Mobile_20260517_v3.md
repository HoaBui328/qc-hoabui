# KIỂM TRA CMR PHÂN HỆ MOBILE — SO VỚI CHUẨN CHUNG HỆ THỐNG

**Tiêu đề:** Phân tích đồng nhất CMR Mobile vs. Chuẩn chung hệ thống  
**Ngày tạo:** 17/05/2026  
**Cập nhật:** 17/05/2026  
**Tác giả:** Antigravity (AI Assistant)  
**Phiên bản:** v3  
**Nguồn:** `CMR_Mobile.md` (v1.6)

> **v3 — Thay đổi so với v2:**
> - Bổ sung **STD-04b**: Placeholder search box → `"Tìm kiếm nhanh theo [điều kiện tìm kiếm]"` — rule này đang thiếu trong CMR Mobile
> - **STD-08 "Không cắt thập phân"**: Vẫn áp dụng cho Mobile (CMR-11 hiện đang cắt trailing zeros → cần sửa). Chỉ bỏ rule max 18 ký tự.

---

## 1. CHUẨN CHUNG HỆ THỐNG (MỚI BỔ SUNG)

| # | Rule | Nội dung chuẩn | Phạm vi |
|---|------|----------------|---------| 
| STD-01 | Filter dropdown default | Tất cả **filter** dropdown có option **"Tất cả"** — Mặc định chọn "Tất cả" | Chỉ filter |
| STD-02a | Message lỗi required — dropdown | **"Vui lòng chọn [tên trường]"** | Dropdown/Radio |
| STD-02b | Message lỗi required — text/numeric | **"Vui lòng nhập [tên trường]"** | Text/Numeric field |
| STD-03 | Placeholder dropdown | **"Chọn [tên trường]"** | Form dropdown |
| STD-04a | Placeholder text/numeric field | **"Nhập [tên trường]"** | Text/Numeric field |
| STD-04b | Placeholder search box | **"Tìm kiếm nhanh theo [điều kiện tìm kiếm]"** *(VD: "Tìm kiếm nhanh theo tên KCN")* | Search box |
| STD-05 | Message quá max length | **"[Tên trường] nhập quá ký tự cho phép"** | Tất cả |
| STD-06 | Message chưa đủ min length | **"[Tên trường] nhập chưa đủ ký tự cho phép"** | Tất cả |
| STD-07 | Tab navigation | Nhấn Tab chuyển field *(Chỉ Web/Report — KHÔNG áp dụng Mobile)* | Web/Report |
| STD-08 | Numeric — không cắt thập phân | Không tự cắt phần thập phân người dùng nhập | Tất cả (trừ max 18 ký tự — Mobile giữ 500) |

---

## 2. SO SÁNH CHI TIẾT

### 2.1. STD-01 — Filter Dropdown Default "Tất cả"

> **Phạm vi:** Chỉ áp dụng cho **filter dropdown** (bộ lọc tìm kiếm). Các dropdown trong form nhập liệu không thuộc rule này.

| Hạng mục | Chuẩn chung | CMR Mobile | Kết luận |
|----------|-------------|------------|----------|
| Filter dropdown default | "Tất cả" — mặc định chọn | CMR-02: *"Tất cả dropdown trong bộ lọc mặc định 'Tất cả'"* | ✅ **ĐÃ CÓ** — Đúng phạm vi filter |
| Phạm vi | Chỉ **filter dropdown** | CMR-02 áp dụng cho bộ lọc tìm kiếm | ✅ **ĐÚNG PHẠM VI** |

**➜ Mức độ: ✅ Không cần thay đổi**

---

### 2.2. STD-02 — Message lỗi Required

| Hạng mục | Chuẩn chung | CMR Mobile | Kết luận |
|----------|-------------|------------|----------|
| Required message (dropdown) | **"Vui lòng chọn [tên trường]"** | CMR-03: *"[tên trường] là bắt buộc."* | 🔴 **MÂU THUẪN** |
| Required message (text/numeric) | **"Vui lòng nhập [tên trường]"** | CMR-09: *"[tên trường] là bắt buộc."* | 🔴 **MÂU THUẪN** |

**➜ Mức độ: 🔴 Mâu thuẫn — Cần sửa cả CMR-03 và CMR-09**

---

### 2.3. STD-03/04 — Placeholder

| Hạng mục | Chuẩn chung | CMR Mobile | Kết luận |
|----------|-------------|------------|----------|
| Placeholder dropdown (form) | "Chọn [tên trường]" | CMR-03: *"Chọn..."* (generic) | 🔴 **MÂU THUẪN** |
| Placeholder text/numeric | "Nhập [tên trường]" | Không có rule tổng quát | ❌ **THIẾU** |
| Placeholder search box | **"Tìm kiếm nhanh theo [điều kiện]"** *(VD: "Tìm kiếm nhanh theo tên KCN")* | CMR-01: Có placeholder ví dụ nhưng không có rule chuẩn | ❌ **THIẾU RULE** |

> **Ví dụ placeholder search box theo UC Mobile:**
> - "Tìm kiếm nhanh theo tên KCN"
> - "Tìm kiếm nhanh theo tên doanh nghiệp"
> - "Tìm kiếm nhanh theo tên thủ tục"

**➜ Mức độ: 🔴 Mâu thuẫn & Thiếu rule**

---

### 2.4. STD-05/06 — Message Max/Min Length

| Hạng mục | Chuẩn chung | CMR Mobile | Kết luận |
|----------|-------------|------------|----------|
| Message quá max length | "[Tên trường] nhập quá ký tự cho phép" | Không có | ❌ **THIẾU** |
| Message chưa đủ min length | "[Tên trường] nhập chưa đủ ký tự cho phép" | Không có | ❌ **THIẾU** |

**➜ Mức độ: ❌ Thiếu — Cần bổ sung vào CMR-09 (và CMR-11 cho numeric)**

---

### 2.5. STD-07 — Tab Navigation

| Hạng mục | Chuẩn chung | CMR Mobile | Kết luận |
|----------|-------------|------------|----------|
| Tab navigation | Chỉ Web/Report | Không có (đúng với Mobile) | ✅ **KHÔNG CẦN** |

---

### 2.6. STD-08 — Numeric: Không cắt thập phân

> **Lưu ý phân biệt với Report:**
> - **Max 18 ký tự** → **KHÔNG áp dụng Mobile** — giữ CMR-11: default 500 ký tự
> - **Không cắt thập phân** → **CÓ áp dụng Mobile** — CMR-11 hiện đang cắt trailing zeros → cần sửa

| Hạng mục | Áp dụng Mobile? | CMR Mobile hiện tại | Kết luận |
|----------|----------------|---------------------|----------|
| Max 18 ký tự numeric | ❌ Không áp dụng | CMR-11: 500 ký tự | ✅ Giữ nguyên 500 ký tự |
| Không cắt thập phân | ✅ **Có áp dụng** | CMR-11: *"Tự động cắt bỏ các số 0 vô nghĩa ở cuối"* | 🔴 **MÂU THUẪN** — Cần sửa CMR-11 |

**➜ Mức độ: 🔴 Mâu thuẫn — Sửa CMR-11: bỏ hành vi cắt trailing zeros**

---

## 3. BẢNG TỔNG HỢP GAP

| # | Rule | CMR Mobile hiện tại | Chuẩn chung | Loại Gap |
|---|------|---------------------|-------------|----------|
| G1 | Filter default "Tất cả" | CMR-02: Đúng — chỉ filter | Chỉ filter dropdown | ✅ Không cần sửa |
| G2 | Placeholder dropdown form | CMR-03: "Chọn..." | "Chọn [tên trường]" | 🔴 Mâu thuẫn |
| G3 | Required message dropdown | CMR-03: "[tên trường] là bắt buộc." | "Vui lòng chọn [tên trường]" | 🔴 Mâu thuẫn |
| G4 | Required message text/numeric | CMR-09: "[tên trường] là bắt buộc." | "Vui lòng nhập [tên trường]" | 🔴 Mâu thuẫn |
| G5 | Placeholder text/numeric | Không có rule | "Nhập [tên trường]" | ❌ Thiếu hoàn toàn |
| G6 | Placeholder search box | CMR-01 chỉ có ví dụ, không có rule chuẩn | "Tìm kiếm nhanh theo [điều kiện]" | ❌ Thiếu rule |
| G7 | Message quá max length | Không có | "[Tên trường] nhập quá ký tự cho phép" | ❌ Thiếu hoàn toàn |
| G8 | Message chưa đủ min length | Không có | "[Tên trường] nhập chưa đủ ký tự cho phép" | ❌ Thiếu hoàn toàn |
| G9 | Tab navigation | Không có | Không áp dụng Mobile | ✅ Đúng |
| G10 | Numeric — không cắt thập phân | CMR-11: Cắt trailing zeros | Không tự cắt | 🔴 Mâu thuẫn |
| G11 | Numeric max length | Không áp dụng STD-08 | Giữ CMR-11: 500 ký tự | ✅ Không thay đổi |

**Tổng:** 4 mâu thuẫn 🔴 | 4 thiếu ❌ | 3 đúng ✅

---

## 4. UC BỊ ẢNH HƯỞNG

> **Nguồn:** Commit `1dec2dc` — 17/05/2026 *"BA update CMR mobile và report"*  
> Gồm **27 UC Mobile** và **52 nhóm UC Report** được cập nhật đồng loạt.

---

### 4.1 SRS-Mobile

#### G6 — Placeholder search box

| UC | Tên chức năng | Ví dụ placeholder chuẩn |
|----|---------------|--------------------------|
| UC2 | Tra cứu KCN | "Tìm kiếm nhanh theo tên KCN" |
| UC7-11 | Khai thác TT Khu kinh tế | "Tìm kiếm nhanh theo tên KKT" |
| UC12-16 | Khai thác TT Mô hình khu khác | "Tìm kiếm nhanh theo tên khu" |
| UC17-21 | Khai thác TT KCN Sinh thái | "Tìm kiếm nhanh theo tên KCNST" |
| UC22-26 | Khai thác TT Khu phi thuế quan | "Tìm kiếm nhanh theo tên khu PTQ" |
| UC27-31 | Khai thác TT Khu thương mại tự do | "Tìm kiếm nhanh theo tên KTMTD" |
| UC40 | Tra cứu đất KCN | "Tìm kiếm nhanh theo tên thửa đất" |
| UC41 | Tra cứu thuê đất KCN | "Tìm kiếm nhanh theo tên thửa đất" |
| UC45-51 | Quản lý hồ sơ | "Tìm kiếm nhanh theo số hồ sơ" |
| UC53/63-65 | Phản ánh kiến nghị | "Tìm kiếm nhanh theo tiêu đề phản ánh" |
| UC54 | Báo cáo đã nộp | "Tìm kiếm nhanh theo tên báo cáo" |
| UC55 | Chuyển trang đầu tư | "Tìm kiếm nhanh theo tên dự án" |
| UC56-57/66/68 | Tin tức | "Tìm kiếm nhanh theo tiêu đề tin" |
| UC58 | Tra cứu thủ tục đầu tư | "Tìm kiếm nhanh theo tên thủ tục" |
| UC59 | Tra cứu báo cáo đầu tư | "Tìm kiếm nhanh theo tên báo cáo" |
| UC62 | Tra cứu doanh nghiệp | "Tìm kiếm nhanh theo tên doanh nghiệp" |
| UC69 | Tra cứu văn bản pháp luật | "Tìm kiếm nhanh theo tên văn bản" |
| UC70 | Tra cứu TTHC | "Tìm kiếm nhanh theo tên thủ tục" |
| UC87 | Tra cứu dự án kêu gọi ĐT | "Tìm kiếm nhanh theo tên dự án" |
| UC90 | Xúc tiến đầu tư | "Tìm kiếm nhanh theo tên sự kiện" |

#### G2 + G3 + G4 + G5 + G7 + G8 — Placeholder & Required message (form nhập liệu)

| UC | Tên chức năng | Loại trường |
|----|---------------|-------------|
| UC42-44 | Quản lý đặt lịch | Dropdown + Text |
| UC45-51 | Quản lý hồ sơ | Dropdown + Text + Numeric |
| UC53/63-65 | Phản ánh kiến nghị | Dropdown + Text |
| UC249 | Quản lý thông tin tài khoản cá nhân | Dropdown + Text |
| UC250 | Quản lý tài khoản doanh nghiệp | Dropdown + Text |
| UC251 | Đổi mật khẩu | Text |
| UC252 | Đăng ký tài khoản | Dropdown + Text |
| UC253 | Gửi thông tin quên mật khẩu | Text |
| UC256 | Đăng nhập Mobile | Text |

#### G10 — Numeric không cắt thập phân

| UC | Tên chức năng | Trường số bị ảnh hưởng |
|----|---------------|------------------------|
| UC2 | Tra cứu KCN | Diện tích, số liệu KCN |
| UC7-11 | Khai thác TT Khu kinh tế | Số liệu KKT |
| UC12-16 | Khai thác TT Mô hình khu khác | Số liệu |
| UC17-21 | Khai thác TT KCN Sinh thái | Số liệu |
| UC22-26 | Khai thác TT Khu phi thuế quan | Số liệu |
| UC27-31 | Khai thác TT Khu thương mại tự do | Số liệu |
| UC40 | Tra cứu đất KCN | Diện tích đất |
| UC41 | Tra cứu thuê đất KCN | Diện tích, giá thuê |
| UC45-51 | Quản lý hồ sơ | Số tiền trong hồ sơ |

---

### 4.2 SRS-Report

> Toàn bộ **52 nhóm UC Report** dưới đây đều bị ảnh hưởng bởi **G2/G3/G4** (placeholder & required message), **G5/G7/G8** (message max/min length), **G6** (placeholder search box), **G10** (numeric không cắt thập phân).

| UC | Tên chức năng |
|----|---------------|
| UC011-034 | Bộ Hồ sơ Xúc tiến Đầu tư |
| UC035-040 | Báo cáo trước khi thực hiện dự án ĐT |
| UC041-046 | Báo cáo tình hình thực hiện dự án ĐT Quý |
| UC047-052 | Thực hiện Dự án Đầu tư |
| UC053-058 | Đầu kỳ Dự án Đầu tư |
| UC059-064 | Đầu kỳ Đầu tư |
| UC065-070 | Tổng hợp ĐTNN Địa bàn |
| UC071-088 | Bộ Hồ sơ Báo cáo ĐTNN Địa bàn |
| UC089-094 | Cấp mới GCNĐKĐT |
| UC095-100 | Điều chỉnh GCNĐKĐT |
| UC101-106 | Tạm ngưng/Chấm dứt ĐTNN |
| UC107-112 | Báo cáo Tổng hợp Xuất Nhập Khẩu |
| UC113-118 | Xuất khẩu ĐTNN |
| UC119-124 | Nhập khẩu ĐTNN |
| UC125-130 | Tài chính Địa bàn ĐTNN |
| UC131-136 | Tài chính Doanh nghiệp ĐTNN |
| UC137-142 | Lao động Nước ngoài (Quốc tịch) |
| UC143-148 | Lao động Nước ngoài (Địa bàn) |
| UC149-154 | Chuyển giao Công nghệ Địa bàn |
| UC155-160 | Giao đất/Cho thuê đất |
| UC161-166 | Báo cáo 6 tháng ĐTRNN |
| UC167-172 | Thông báo ĐTRNN |
| UC173-178 | Kéo thời hạn Chuyển lợi nhuận |
| UC179-184 | Chấm dứt Hoạt động ĐTRNN |
| UC185-190 | Báo cáo năm ĐTRNN |
| UC191-196 | Báo cáo năm Tài chính ĐTRNN |
| UC197-202 | Vay vốn TCKTNNN |
| UC203-208 | QLNN Bộ ĐTRNN |
| UC209-214 | ĐKGDNH Chấm dứt ĐTRNN |
| UC215-220 | Chuyển vốn ĐTRNN |
| UC239-244 | Thu hút Đầu tư KCN |
| UC245-250 | Thành lập/Điều chỉnh KCN |
| UC251-256 | Thực hiện Dự án Hạ tầng KCN |
| UC257-262 | SXKD tại KCN |
| UC263-268 | Nhà máy XLNT KCN |
| UC269-274 | Lao động KCN |
| UC275-280 | Danh mục KCN Quy hoạch |
| UC281-286 | Số lượng Diện tích KKT |
| UC287-292 | Thu hút Đầu tư KKT |
| UC293-298 | Quy hoạch đất KKT |
| UC299-304 | Biểu Tổng hợp KKT |
| UC305-310 | Biểu Khu phi thuế quan |
| UC311-316 | Báo cáo KCN/KKT |
| UC317-322 | Đầu tư theo Đối tác KCN |
| UC323-328 | Điều chỉnh Dự án KCN |
| UC329-334 | Thu hồi Dự án KCN |
| UC335-340 | Chỉ số Đánh giá Hiệu quả KCNST |
| UC341-346 | Giám sát KCN Sinh thái |
| UC347-352 | Chỉ số Đánh giá DN Sinh thái |
| UC353-358 | Giám sát DN Sinh thái |
| UC364-366 | Quản lý Báo cáo Đã nộp |
| UC367-372 | Quản lý Báo cáo NDT Địa phương nộp |

---

## 5. KHUYẾN NGHỊ CẬP NHẬT CMR MOBILE

| # | CMR cần sửa | Before | After | Ưu tiên |
|---|-------------|--------|-------|---------|
| 1 | CMR-03 — Placeholder dropdown | `"Chọn..."` | `"Chọn [tên trường]"` | 🔴 Cao |
| 2 | CMR-03 — Required message dropdown | `"[tên trường] là bắt buộc."` | `"Vui lòng chọn [tên trường]"` | 🔴 Cao |
| 3 | CMR-09 — Required message text/numeric | `"[tên trường] là bắt buộc."` | `"Vui lòng nhập [tên trường]"` | 🔴 Cao |
| 4 | CMR-09 — Thêm Placeholder text/numeric | (Không có) | `"Nhập [tên trường]"` | 🔴 Cao |
| 5 | CMR-01 — Chuẩn hoá Placeholder search box | Chỉ có ví dụ không có rule chuẩn | `"Tìm kiếm nhanh theo [điều kiện tìm kiếm]"` | 🔴 Cao |
| 6 | CMR-09 — Thêm message max length | (Không có) | `"[Tên trường] nhập quá ký tự cho phép"` | 🔴 Cao |
| 7 | CMR-09 — Thêm message min length | (Không có) | `"[Tên trường] nhập chưa đủ ký tự cho phép"` | ⚠️ TB |
| 8 | CMR-11 — Không cắt thập phân | `"Tự động cắt bỏ các số 0 vô nghĩa ở cuối"` | `"Không tự cắt phần thập phân người dùng nhập"` | 🔴 Cao |
| 9 | CMR-11 — Numeric max length | Giữ nguyên `500 ký tự` | *(Không đổi)* | — |

---

*Kết thúc. Phiên bản: v3 — 17/05/2026*
