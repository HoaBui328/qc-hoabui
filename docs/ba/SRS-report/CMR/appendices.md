# Phụ lục: Danh mục Báo cáo & Quy tắc Đặt Tên (Appendices)

> **Nguồn gốc:** Soát và chuẩn hóa từ file `Appendices.xlsx` + nội dung từng UC file.
> **Ngày cập nhật:** 2026-05-22 | **Phiên bản:** 2.1

---

## 1. Quy tắc Prefix Mã Báo cáo

Mã báo cáo được tạo tự động theo cú pháp:

```
[PREFIX]_[MãBiểu]_[ID]
```

| Phân hệ | Prefix | Mô tả phân hệ | Mã biểu đặc trưng |
|---|---|---|---|
| **FDI** | `FDI_` | Đầu tư nước ngoài vào Việt Nam | A.III.x, A.IV.x |
| **ODI** | `ODI_` | Đầu tư ra nước ngoài | I.x, II.x |
| **DDI** | `DDI_` | Đầu tư trong nước | A.I.x, A.II.x (TBD) |
| **EZ** | `EZ_` | Quản lý khu công nghiệp, khu kinh tế | 2101–2116.H.QLKKT, A.4, B.4 |
| **PROM** | `PROM_` | Xúc tiến đầu tư | B.IV.x |

> [!IMPORTANT]
> Prefix `DTNN_` là **sai** — không được sử dụng. Toàn bộ file SRS đang dùng `DTNN_` cần được cập nhật về `FDI_` (xem mục 4 — Lịch sử thay đổi).

---

## 2. Danh sách Mã Báo cáo theo Phân hệ

### 2.1 Phân hệ PROM — Xúc tiến đầu tư

| Mã UC | Tên Báo cáo | Mã biểu | Mã tự sinh (ví dụ) |
|---|---|---|---|
| UC011-034 | Bộ hồ sơ báo cáo xúc tiến đầu tư | II.4.2 / II.4.3 / II.4.4 / I.4.4 | `PROM_[II42/II43/II44/I44]_[ID]` |

> [!NOTE]
> Nhóm PROM hiện chỉ xác nhận UC011-034. Các nhóm báo cáo PROM khác (nếu có) cần BA bổ sung vào bảng này.

---

### 2.2 Phân hệ FDI — Đầu tư nước ngoài vào Việt Nam

#### Nhóm A.III — Báo cáo dự án FDI cụ thể

| Mã UC | Tên Báo cáo | Mã biểu | Mã tự sinh |
|---|---|---|---|
| UC035-040 | Báo cáo trước khi thực hiện dự án đầu tư *(phục vụ cả FDI lẫn DDI — cùng UC, cùng mẫu biểu A.III.3, tên và nội dung có thể giống hoặc khác theo phân hệ)* | A.III.3 | `FDI_AIII3_[ID]` |
| UC041-046 | Báo cáo tình hình thực hiện dự án đầu tư — Quý | A.III.3 | `FDI_AIII3_[ID]` |
| UC047-052 | Báo cáo tình hình thực hiện dự án đầu tư — Năm | A.III.2 | `FDI_AIII2_[ID]` |
| UC053-058 | Báo cáo tình hình thực hiện dự án đầu tư dầu khí — Quý (Mẫu A.III.4) | A.III.4 | `FDI_AIII4_[ID]` |
| UC059-064 | Báo cáo tình hình thực hiện dự án hợp tác dầu khí — Năm (Mẫu A.III.5) | A.III.5 | `FDI_AIII5_[ID]` |

#### Nhóm A.IV — Báo cáo tổng hợp ĐTNN theo địa bàn

| Mã UC | Tên Báo cáo | Mã biểu | Mã tự sinh |
|---|---|---|---|
| UC065-070 | Báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/TP — Quý (Mẫu A.IV.1) | A.IV.1 | `FDI_AIV1_[ID]` |
| UC071-076 | Văn bản báo cáo thu hút ĐTNN trên địa bàn tỉnh/TP — Năm (Mẫu A.IV.2) | A.IV.2 | `FDI_AIV2_[ID]` |
| UC071-088 | Bộ hồ sơ báo cáo ĐTNN địa bàn (A.IV.2 / A.IV.3 / A.IV.4) — Báo cáo gộp | A.IV.2, A.IV.3, A.IV.4 | `FDI_[AIV2/AIV3/AIV4]_[ID]` *(mã bộ hồ sơ kết hợp theo từng biểu, tương tự pattern PROM_[II42/II43/II44/I44]_[ID])* |
| UC077-082 | Báo cáo về tình hình ĐTNN trên địa bàn tỉnh/TP — Năm (Mẫu A.IV.3) | A.IV.3 | `FDI_AIV3_[ID]` |
| UC083-088 | Danh mục dự án ĐTNN đang có nhà đầu tư quan tâm (Mẫu A.IV.4) | A.IV.4 | `FDI_AIV4_[ID]` |
| UC089-094 | Báo cáo cấp mới GCNĐKĐT cho NĐT nước ngoài — Quý (Mẫu A.IV.5) | A.IV.5 | `FDI_AIV5_[ID]` |
| UC095-100 | Báo cáo điều chỉnh GCNĐKĐT cho NĐT nước ngoài — Quý (Mẫu A.IV.6) | A.IV.6 | `FDI_AIV6_[ID]` |
| UC101-106 | Báo cáo tạm ngừng, chấm dứt dự án ĐTNN — Quý (Mẫu A.IV.7) | A.IV.7 | `FDI_AIV7_[ID]` |
| UC107-112 | Báo cáo tổng hợp xuất nhập khẩu TCKT ĐTNN (Mẫu A.IV.8a) | A.IV.8a | `FDI_AIV8A_[ID]` |
| UC113-118 | Báo cáo tình hình xuất khẩu của TCKT có vốn ĐTNN — Năm (Mẫu A.IV.8b) | A.IV.8b | `FDI_AIV8B_[ID]` |
| UC119-124 | Báo cáo tình hình nhập khẩu của TCKT có vốn ĐTNN — Năm (Mẫu A.IV.8c) | A.IV.8c | `FDI_AIV8C_[ID]` |
| UC125-130 | Báo cáo tổng hợp tài chính và nộp ngân sách TCKT ĐTNN theo địa bàn — Năm (Mẫu A.IV.9a) | A.IV.9a | `FDI_AIV9A_[ID]` |
| UC131-136 | Báo cáo tổng hợp tài chính và nộp ngân sách TCKT ĐTNN theo doanh nghiệp — Năm (Mẫu A.IV.9b) | A.IV.9b | `FDI_AIV9B_[ID]` |
| UC137-142 | Báo cáo lao động nước ngoài tại TCKT ĐTNN theo quốc tịch — Năm (Mẫu A.IV.10a) | A.IV.10a | `FDI_AIV10A_[ID]` |
| UC143-148 | Báo cáo lao động nước ngoài tại TCKT ĐTNN theo địa bàn — Năm (Mẫu A.IV.10b) | A.IV.10b | `FDI_AIV10B_[ID]` |
| UC149-154 | Báo cáo chuyển giao công nghệ tại TCKT ĐTNN theo địa bàn — Năm (Mẫu A.IV.11) | A.IV.11 | `FDI_AIV11_[ID]` |
| UC155-160 | Báo cáo tình hình giao đất, cho thuê đất đối với TCKT ĐTNN trên địa bàn tỉnh/TP (Mẫu A.IV.12) | A.IV.12 | `FDI_AIV12_[ID]` |

---

### 2.3 Phân hệ ODI — Đầu tư ra nước ngoài

| Mã UC | Tên Báo cáo | Mã biểu | Mã tự sinh |
|---|---|---|---|
| UC161-166 | Báo cáo định kỳ 6 tháng tình hình hoạt động dự án ĐTRNN | I.15 | `ODI_I15_[ID]` |
| UC167-172 | Thông báo thực hiện hoạt động đầu tư ở nước ngoài | I.10 | `ODI_I10_[ID]` |
| UC173-178 | Thông báo kéo dài thời hạn chuyển lợi nhuận dự án ĐTRNN về Việt Nam | I.11 | `ODI_I11_[ID]` |
| UC179-184 | Thông báo chấm dứt hoạt động đầu tư ra nước ngoài | I.20 | `ODI_I20_[ID]` |
| UC185-190 | Báo cáo định kỳ năm tình hình hoạt động dự án ĐTRNN | I.16 | `ODI_I16_[ID]` |
| UC191-196 | Báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính | I.17 | `ODI_I17_[ID]` |
| UC197-202 | Báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn | I.19 | `ODI_I19_[ID]` |
| UC203-208 | Báo cáo tình hình quản lý nhà nước về hoạt động ĐTRNN của các Bộ, ngành | II.4 | `ODI_II4_[ID]` |
| UC209-214 | Báo cáo về tình hình đăng ký giao dịch ngoại hối và chấm dứt ĐTRNN (Mẫu II.5) | II.5 | `ODI_II5_[ID]` |
| UC215-220 | Báo cáo về tình hình chuyển vốn đầu tư ra nước ngoài (Mẫu II.6) | II.6 | `ODI_II6_[ID]` |

---

### 2.4 Phân hệ DDI — Đầu tư trong nước

> **Lưu ý:** Các UC DDI (UC221–238) là nhóm **riêng biệt** — không trùng với FDI. Tên báo cáo có thể giống, mã biểu có thể tương tự, nhưng đây là các Use Case độc lập của phân hệ DDI.

| Mã UC | Tên Báo cáo | Mã biểu DDI | Mã tự sinh |
|---|---|---|---|
| UC221-226 | Báo cáo tình hình thực hiện dự án đầu tư trong nước — Quý | A.III.1 | `DDI_AIII1_[ID]` |
| UC227-231 | Báo cáo tình hình thực hiện dự án đầu tư trong nước — Năm | A.III.2 | `DDI_AIII2_[ID]` |
| UC233-238 | Báo cáo trước khi thực hiện dự án đầu tư trong nước | A.III.3 | `DDI_AIII3_[ID]` |

> [!NOTE]
> Dải UC đã được BA xác nhận (2026-05-21). UC221-226 = Quý, UC227-231 = Năm, UC233-238 = Trước khi thực hiện.

---

### 2.5 Phân hệ EZ — Quản lý KCN, KKT

| Mã UC | Tên Báo cáo | Mã biểu | Mã tự sinh |
|---|---|---|---|
| UC239-244 | Tình hình thu hút đầu tư vào KCN trong kỳ báo cáo | 2101.H.QLKKT | `EZ_2101HQLKKT_[ID]` |
| UC245-250 | Tình hình thành lập mới, điều chỉnh diện tích và thu hồi KCN | 2102.H.QLKKT | `EZ_2102HQLKKT_[ID]` |
| UC251-256 | Tình hình thực hiện dự án đầu tư xây dựng kết cấu hạ tầng KCN | 2103.H.QLKKT | `EZ_2103HQLKKT_[ID]` |
| UC257-262 | Tình hình hoạt động sản xuất kinh doanh tại KCN lũy kế | 2104.H.QLKKT | `EZ_2104HQLKKT_[ID]` |
| UC263-268 | Tình hình đầu tư và xây dựng nhà máy xử lý nước thải tập trung KCN | 2105.H.QLKKT | `EZ_2105HQLKKT_[ID]` |
| UC269-274 | Số lao động trực tiếp làm việc tại các KCN | 2106.H.QLKKT | `EZ_2106HQLKKT_[ID]` |
| UC275-280 | Danh mục các KCN nằm trong quy hoạch còn hiệu lực | 2107.H.QLKKT | `EZ_2107HQLKKT_[ID]` |
| UC281-286 | Số lượng và diện tích các khu kinh tế | 2108.H.QLKKT | `EZ_2108HQLKKT_[ID]` |
| UC287-292 | Tình hình thu hút đầu tư tại KKT trong kỳ báo cáo | 2109.H.QLKKT | `EZ_2109HQLKKT_[ID]` |
| UC293-298 | Tình hình quy hoạch, sử dụng đất tại KKT | 2110.H.QLKKT | `EZ_2110HQLKKT_[ID]` |
| UC299-304 | Tình hình thu hút dự án ĐT xây dựng kết cấu hạ tầng trong KKT lũy kế | 2111.H.QLKKT | `EZ_2111HQLKKT_[ID]` |
| UC305-310 | Tình hình hoạt động của khu phi thuế quan, khu thương mại tự do lũy kế | 2112.H.QLKKT | `EZ_2112HQLKKT_[ID]` |
| UC311-316 | Tình hình thu hút dự án ĐT sản xuất kinh doanh trong KKT lũy kế | 2113.H.QLKKT | `EZ_2113HQLKKT_[ID]` |
| UC317-322 | Tình hình ĐTNN vào KCN, KKT phân theo đối tác đầu tư lũy kế | 2114.H.QLKKT | `EZ_2114HQLKKT_[ID]` |
| UC323-328 | Tình hình điều chỉnh quyết định chủ trương ĐT/GCNĐKĐT tại KCN, KKT | 2115.H.QLKKT | `EZ_2115HQLKKT_[ID]` |
| UC329-334 | Tình hình thu hồi quyết định chủ trương ĐT/GCNĐKĐT tại KCN, KKT | 2116.H.QLKKT | `EZ_2116HQLKKT_[ID]` |
| UC341-346 | Báo cáo theo dõi, giám sát thực hiện KCN sinh thái (khoản 1 Điều 43 NĐ 35/2022) | A.4 | `EZ_A4_[ID]` |
| UC353-358 | Báo cáo theo dõi, giám sát thực hiện doanh nghiệp sinh thái (khoản 2 Điều 43 NĐ 35/2022) | B.4 | `EZ_B4_[ID]` |

---

## 3. Danh sách Mã cơ quan nộp (Agency Codes)

| Mã cơ quan | Tên cơ quan / Tổ chức | Ghi chú |
|---|---|---|
| **BKHĐT** | Bộ Kế hoạch và Đầu tư | Cơ quan quản lý cấp cao nhất |
| **BQLKCN** | Ban Quản lý Khu công nghiệp, Khu kinh tế | Quản lý theo địa bàn KCN/KKT |
| **UBND** | Ủy ban Nhân dân tỉnh/thành phố | Quản lý theo địa bàn hành chính |
| **SKHĐT** | Sở Kế hoạch và Đầu tư | Cơ quan quản lý cấp tỉnh/thành phố |
| **TCKT** | Tổ chức kinh tế | Doanh nghiệp/Tổ chức kinh tế phụ trách dự án |
| **NDT** | Nhà đầu tư | Nhà đầu tư độc lập / thành viên |
| **BCT** | Bộ Công Thương | Quản lý ngành (nếu có) |
| **BTC** | Bộ Tài chính | Quản lý ngành (nếu có) |
| **BXD** | Bộ Xây dựng | Quản lý ngành (nếu có) |
| **NHNN** | Ngân hàng Nhà nước | Quản lý ngoại hối / chuyển vốn |

> **Lưu ý:** Đối với báo cáo do TCKT hoặc NDT nộp, file export sử dụng Mã-dự-án thay vì Mã-cơ-quan-nộp (Tham chiếu: CF_04). Nếu báo cáo thuộc loại Bộ hồ sơ, hệ thống sử dụng Mã bộ hồ sơ kết hợp với mã của từng biểu bên trong.

---

## 4. Lịch sử Thay đổi & Lỗi Đã Phát Hiện

### v2.0 — 2026-05-11

**Nguồn soát:** `Appendices.xlsx` + scan metadata toàn bộ 52 UC file.

#### 4.1 Lỗi Prefix trong các SRS file

Kết quả scan thực tế toàn bộ UC files (2026-05-11):

| UC | Mã hiện tại trong SRS file | Mã đúng | Vấn đề |
|---|---|---|---|
| UC035-040 | `[FDI]_AIII3_[ID]` | `FDI_AIII3_[ID]` | Dư dấu `[]` bao prefix |
| UC041-046 | `DTNN_A3_1_[ID]` | `FDI_AIII1_[ID]` | Sai prefix DTNN→FDI; sai mã A3→AIII |
| UC047-052 | `DTNN_A3_2_[ID]` | `FDI_AIII2_[ID]` | Sai prefix DTNN→FDI; sai mã A3→AIII |
| UC053-058 | `DTNN_A3_4_[ID]` | `FDI_AIII4_[ID]` | Sai prefix DTNN→FDI; sai mã A3→AIII |
| UC059-064 | `DTNN_A3_5_[ID]` | `FDI_AIII5_[ID]` | Sai prefix DTNN→FDI; sai mã A3→AIII |
| UC065-070 | `DTNN_A4_1_[ID]` | `FDI_AIV1_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC071-076 | `DTNN_A4_2_[ID]` | `FDI_AIV2_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC071-088 | `Tham chiếu: CMR_09` | `FDI_[AIV2/AIV3/AIV4]_[ID]` | Chưa ghi mã cụ thể |
| UC077-082 | `DTNN_A4_3_[ID]` | `FDI_AIV3_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC083-088 | `DTNN_A4_4_[ID]` | `FDI_AIV4_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC089-094 | `FDI_A4_5_[ID]` | `FDI_AIV5_[ID]` | Sai mã A4→AIV |
| UC095-100 | `DTNN_A4_6_[ID]` | `FDI_AIV6_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV; thừa ghi chú trong cùng dòng |
| UC101-106 | `DTNN_A4_7_[ID]` | `FDI_AIV7_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC107-112 | `DTNN_A4_8A_[ID]` | `FDI_AIV8A_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC113-118 | `DTNN_A4_8B_[ID]` | `FDI_AIV8B_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC119-124 | `DTNN_A4_8C_[ID]` | `FDI_AIV8C_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC125-130 | `DTNN_A4_9a_[ID]` | `FDI_AIV9A_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV; sai hoa/thường |
| UC131-136 | `DTNN_A4_9B_[ID]` | `FDI_AIV9B_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC137-142 | `DTNN_A4_10a_[ID]` | `FDI_AIV10A_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV; sai hoa/thường |
| UC143-148 | `DTNN_A4_10b_[ID]` | `FDI_AIV10B_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV; sai hoa/thường |
| UC149-154 | `DTNN_A4_11_[ID]` | `FDI_AIV11_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |
| UC155-160 | `DTNN_A4_12_[ID]` | `FDI_AIV12_[ID]` | Sai prefix DTNN→FDI; sai mã A4→AIV |

**Các UC đã đúng (không cần sửa):** UC011-034, UC161–220, UC239–358 (đã sửa 3 file EZ trong phiên này).



#### 4.2 Lỗi Phân hệ trong appendices.md cũ (v1.0)

| UC | Phân hệ cũ (sai) | Phân hệ đúng | Căn cứ |
|---|---|---|---|
| UC161-166 | FDI | **ODI** | Nội dung = "đầu tư tại nước ngoài"; mã I.15 |
| UC167-172 | FDI | **ODI** | Nội dung = "thông báo ĐTRNN"; mã I.10 |
| UC185-190 | FDI | **ODI** | Nội dung = "báo cáo năm ĐTRNN"; mã I.16 |
| UC197-202 | FDI | **ODI** | Nội dung = "cho vay vốn tổ chức ở nước ngoài"; mã I.19 |

#### 4.3 Câu hỏi mở đã được BA xác nhận (2026-05-11)

| # | Câu hỏi | Trả lời của BA |
|---|---|---|
| Q1 | UC035-040 áp dụng FDI hay DDI hay cả hai? | **Cả FDI lẫn DDI** — cùng UC, tên báo cáo giống nhau, nội dung có thể giống hoặc khác theo phân hệ |
| Q2 | DDI có UC riêng không? | **Không** — DDI có 3 mã báo cáo (A.I.1, A.I.2, A.I.3) nhưng không có UC riêng; được phục vụ chung UC với FDI |
| Q3 | PROM có thêm UC nào ngoài UC011-034? | **Không** — UC011-034 là UC duy nhất của phân hệ PROM |

#### 4.4 Lỗi thiếu dòng "Quy tắc sinh mã báo cáo" trong SRS file (EZ)

Các UC EZ sau có Mẫu biểu nhưng **chưa có dòng `Quy tắc sinh mã báo cáo`** trong bảng metadata của SRS file:

| UC | Mẫu biểu trong file | Mã cần bổ sung |
|---|---|---|
| UC317-322 | 2114.H.QLKKT | `EZ_2114HQLKKT_[ID]` |
| UC323-328 | 2115.H.QLKKT | `EZ_2115HQLKKT_[ID]` |
| UC329-334 | 2116.H.QLKKT | `EZ_2116HQLKKT_[ID]` |

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-19 | 1.0 → 1.1 | Mục 2.1 — UC011-034 Mã biểu | B.IV.2 / B.IV.3 / B.IV.4 / A.IV.4 | B.4.2 / B.4.3 / B.4.4 / A.IV.4 | Đổi tên mã biểu theo quy ước mới |
| 2026-05-22 | 2.0 → 2.1 | Mục 2.1 — UC011-034 Mã biểu | B.4.2 / B.4.3 / B.4.4 / A.IV.4 | II.4.2 / II.4.3 / II.4.4 / I.4.4 | Đồng bộ với UC011-034 SRS v3.1 |
| 2026-05-22 | 2.0 → 2.1 | Mục 2.1 — UC011-034 Mã tự sinh | `PROM_[BIV2/BIV3/BIV4/AIV4]_[ID]` | `PROM_[II42/II43/II44/I44]_[ID]` | Đồng bộ với UC011-034 SRS v3.1 |
| 2026-05-22 | 2.0 → 2.1 | Mục 2.2 — UC071-088 Ghi chú tham chiếu | tương tự pattern PROM_[BIV2/BIV3/BIV4/AIV4]_[ID] | tương tự pattern PROM_[II42/II43/II44/I44]_[ID] | Cập nhật tham chiếu theo mã mới UC011-034 |
